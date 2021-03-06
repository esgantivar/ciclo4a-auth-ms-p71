"""auth_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from auth_app.views import CrearUsuarioView, DetalleUsuarioView

urlpatterns = [
    path('usuario/', CrearUsuarioView.as_view(), name='usuarios'),
    path('usuario/<int:pk>', DetalleUsuarioView.as_view(), name='usuario'),
    path('manual/', include('auth_app.urls')),
    path('simple/', include('auth_app.urls_simple_jwt'))
]
# re_path() url basadas en expresiones regulares
