from django.http import JsonResponse
import requests
from django.conf import settings
import re

EXCLUDED_URLS = [
    r"^/api/login/$",
    # r"^/account/users/?$",
]


def validate_token(token):
    introspect_url = f"{settings.KEYCLOAK_URL}/introspect"
    payload = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        "token": token,
    }
    response = requests.post(introspect_url, data=payload)
    return response.status_code == 200 and response.json().get("active")


class KeycloakAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow OPTIONS requests (preflight requests for CORS)
        if request.method == "OPTIONS":
            response = JsonResponse({"message": "CORS preflight OK"}, status=200)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
            return response

        # Exclude login URLs
        for pattern in EXCLUDED_URLS:
            if re.match(pattern, request.path):
                return self.get_response(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Unauthorized"}, status=401)

        token = auth_header.split(" ")[1]
        if not validate_token(token):
            return JsonResponse({"error": "Invalid token"}, status=401)

        return self.get_response(request)
