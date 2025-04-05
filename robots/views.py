from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from .models import UserAction
from .serializers import UserActionSerializer
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
import jwt

User = get_user_model()


# save user
class KeycloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None  # No token provided, return AnonymousUser

        token = auth_header.split(" ")[1]  # Extract token from "Bearer <token>"

        # Decode the token (Make sure to verify it using Keycloak's public key)
        try:
            decoded_token = jwt.decode(token,
                                       options={"verify_signature": False})
            username = decoded_token.get("preferred_username")
            email = decoded_token.get("email")
            sub = decoded_token.get("sub")  # Unique Keycloak user ID

            if not username:
                return None  # Invalid token, no username found

            # Check if user exists in Django
            user, created = User.objects.get_or_create(username=username, defaults={"email": email})

            return user, token
        except jwt.ExpiredSignatureError:
            return None
        except jwt.DecodeError:
            return None


class SaveUserActions(APIView):
    authentication_classes = [KeycloakAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = UserActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User actions saved successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from rest_framework import generics
from .models import UserAction
from .serializers import UserActionSerializer


class UserActionCreateView(generics.CreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

# region convertCode

#
# import json
#
#
# def generate_selenium_code(json_data):
#     selenium_code = "from selenium import webdriver\n\n"
#     selenium_code += "driver = webdriver.Chrome()\n\n"
#
#     for action in json_data["actions"]:
#         if action["type"] == "navigate":
#             selenium_code += f'driver.get("{action["url"]}")\n'
#         elif action["type"] == "click":
#             selenium_code += f'driver.find_element_by_css_selector("{action["element"]}").click()\n'
#
#     selenium_code += "\ndriver.quit()"
#     return selenium_code
#
#
# # Example Usage
# json_input = '''
# {
#   "actions": [
#     {"type": "navigate", "url": "https://example.com"},
#     {"type": "click", "element": "#login-button"}
#   ]
# }
# '''
#
# json_data = json.loads(json_input)
# print(generate_selenium_code(json_data))
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("https://example.com")
# driver.find_element_by_css_selector("#login-button").click()
#
# driver.quit()
#
#
#
# from django.core.management.base import BaseCommand
# from robots.models import UserAction
# import json
#
# class Command(BaseCommand):
#     help = 'Generate Selenium code from stored user actions'
#
#     def handle(self, *args, **kwargs):
#         user_actions = UserAction.objects.all()
#         for action in user_actions:
#             selenium_code = generate_selenium_code(action.actions)
#             with open(f"selenium_script_{action.id}.py", "w") as file:
#                 file.write(selenium_code)
#             self.stdout.write(self.style.SUCCESS(f"Generated script for UserAction #{action.id}"))
# endregion
