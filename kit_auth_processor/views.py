from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
# from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from KitAuthProject import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET

import json
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)
    try:
        # Handle both JSON and form-data
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Send request to Keycloak
        payload = {
            "client_id": settings.KEYCLOAK_CLIENT_ID,
            "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
            "grant_type": "password",
            "username": username,
            "password": password,
        }

        response = requests.post(settings.KEYCLOAK_URL, data=payload)

        if response.status_code == 200:
            token_data = response.json()
            return JsonResponse({
                "access_token": token_data.get("access_token"),
                "refresh_token": token_data.get("refresh_token"),
                "expires_in": token_data.get("expires_in"),
                "token_type": token_data.get("token_type"),
            }, status=HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_GET
def protected_view(request):
    return JsonResponse({"message": "This is a protected resource."})
