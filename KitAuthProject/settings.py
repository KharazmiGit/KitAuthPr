import os
from datetime import timedelta
from pathlib import Path
<<<<<<< HEAD

from django.conf.global_settings import MIDDLEWARE
=======
>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
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
    # endregion

    # region framework :
<<<<<<< HEAD
    "corsheaders",
=======

>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
    # API
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',

    # endregion
]

<<<<<<< HEAD

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Move this to the top!
=======
MIDDLEWARE = [
>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<< HEAD
    # "kit_auth_processor.middleware.KeycloakAuthMiddleware",
]


=======
]

>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
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

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#
<<<<<<< HEAD
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'KharazmiDB',
#         'USER': 'CompUser',
#         'PASSWORD': 'qaz@123',
#         'HOST': '192.168.100.206',
#         'PORT': '1433',
#
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }

=======
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'KharazmiDB',
        'USER': 'CompUser',
        'PASSWORD': 'qaz@123',
        'HOST': '192.168.100.206',
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.User'

# region rest-frame-work
REST_FRAMEWORK = {
<<<<<<< HEAD
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
=======
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
    ],
    'DEFAULT_SCHEMA_CLASS':
        'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
# endregion

<<<<<<< HEAD
# region keycloak

KEYCLOAK_URL = "http://localhost:9090/realms/KitAuthRealm/protocol/openid-connect/token"
KEYCLOAK_CLIENT_ID = "KitAuthCliID"
KEYCLOAK_CLIENT_SECRET = "oVZgpYXSM9GlZf8qUadytfgnQp08r8qX"

# endregion

LOGIN_URL = '../admin/'

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
=======

LOGIN_URL = '../admin/'
>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
