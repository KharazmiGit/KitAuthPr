import os
from datetime import timedelta
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6tcu^+@^@%l+cn7*$yb59loh$f^p*^b(hdu-b=atw6ygiiq7@5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # region app :
    'account',
    'kit_auth_processor',
    'robots',
    # endregion

    # region framework :
    "corsheaders",

    # API
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    # endregion
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "kit_auth_processor.middleware.KeycloakAuthMiddleware",
]

ROOT_URLCONF = 'KitAuthProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'KitAuthProject.wsgi.application'

# region db

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'KharazmiDB',
#         'USER': 'CompUser',
#         'PASSWORD': 'qaz@123',
#         'HOST': '192.168.100.206',
#         'PORT': '1433',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

# endregion


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.User'

# REST framework settings
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_simplejwt.auth.JWTAuthentication',
    # ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Keycloak settings
KEYCLOAK_URL = "http://localhost:8080/realms/KitAuthRealm/protocol/openid-connect/token"
KEYCLOAK_CLIENT_ID = "KitAuthCliID"
KEYCLOAK_CLIENT_SECRET = "oVZgpYXSM9GlZf8qUadytfgnQp08r8qX"

# CORS Settings (for Vue frontend)
from corsheaders.defaults import default_headers

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    "Authorization",
    "Content-Type",
]
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

LOGIN_URL = reverse_lazy('auth_processor:login_page')

AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',  # Keycloak authentication
    'django.contrib.auth.backends.ModelBackend',  # Default Django auth
]

# Keycloak Settings
OIDC_RP_CLIENT_ID = "KitAuthCliID"
OIDC_RP_CLIENT_SECRET = "oVZgpYXSM9GlZf8qUadytfgnQp08r8qX"
OIDC_OP_JWKS_ENDPOINT = "http://localhost:8080/realms/KitAuthRealm/protocol/openid-connect/certs"
OIDC_OP_AUTHORIZATION_ENDPOINT = "http://localhost:8080/realms/KitAuthRealm/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = "http://localhost:8080/realms/KitAuthRealm/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = "http://localhost:8080/realms/KitAuthRealm/protocol/openid-connect/userinfo"

# Allow authentication with Keycloak tokens
OIDC_RP_SIGN_ALGO = "RS256"
