"""
URL configuration for KitAuthProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
<<<<<<< HEAD
    path('secure/source/', admin.site.urls),
=======
    path('admin/', admin.site.urls),
>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
    path('api-auth/', include('rest_framework.urls')),

    # region Apps :
    path('account/', include('account.urls')),
<<<<<<< HEAD
    path('', include('kit_auth_processor.urls')),
=======
>>>>>>> 008bbafab7be62588713418cea62f4af91d3648d
    # endregion

    # region Frameworks :
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('All/apis', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # endregion
]
