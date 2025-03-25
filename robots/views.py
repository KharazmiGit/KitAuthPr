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


class SaveUserActionView(APIView):
    authentication_classes = [KeycloakAuthentication]  # Use Keycloak authentication


    def post(self, request):
        serializer = UserActionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "User actions saved successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
