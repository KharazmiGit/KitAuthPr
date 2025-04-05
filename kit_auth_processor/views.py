# Django imports
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect

from django.conf import settings

# Third-party imports
import json
import requests
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            # Handle both JSON and form-data
            if request.content_type == "application/json":
                data = json.loads(request.body)
            else:
                data = request.POST

            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return Response(
                    {"error": "Username and password are required."},
                    status=status.HTTP_400_BAD_REQUEST
                )

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

            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON format"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@require_GET
def protected_view(request):
    return JsonResponse({"message": "This is a protected resource."})


class LoginPageView(View):  # internal !!!
    def get(self, request):
        # Render the login page for GET requests
        return render(request, 'auth/login.html')

    def post(self, request):
        try:
            # Retrieve username and password from the POST data
            username = request.POST.get('username')
            password = request.POST.get('pass')

            if not username or not password:
                return JsonResponse(
                    {"error": "Username and password are required."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            payload = {
                "client_id": settings.KEYCLOAK_CLIENT_ID,
                "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
                "grant_type": "password",
                "username": username,
                "password": password,
            }

            # Authenticate with Keycloak
            keycloak_response = requests.post(settings.KEYCLOAK_URL, data=payload)

            if keycloak_response.status_code == 200:
                token_data = keycloak_response.json()

                json_response = JsonResponse({
                    "message": "Login successful",
                    "redirect_url": reverse('account:index_page')
                }, status=status.HTTP_200_OK)

                # Set cookies for access_token and refresh_token
                json_response.set_cookie(
                    key='access_token',
                    value=token_data.get("access_token"),
                    httponly=True,
                    secure=True,
                    samesite='Lax',
                    max_age=token_data.get("expires_in"),
                    expires=1
                )
                json_response.set_cookie(
                    key='refresh_token',
                    value=token_data.get("refresh_token"),
                    httponly=True,
                    secure=True,
                    samesite='Lax'
                )

                return json_response
            else:
                return JsonResponse(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def revoke_token(refresh_token):
    revoke_url = f"{settings.KEYCLOAK_URL}/logout"
    payload = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        "refresh_token": refresh_token,
    }
    response = requests.post(revoke_url, data=payload)
    return response.status_code == 204  # 204 No Content indicates success


def logout_view(request):
    # Retrieve the refresh token from cookies
    refresh_token = request.COOKIES.get('refresh_token')

    # Invalidate the token on Keycloak
    if refresh_token:
        revoke_token(refresh_token)

    # Create a response to redirect to the login page
    response = redirect('/login/')

    # Clear the cookies
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    return response
