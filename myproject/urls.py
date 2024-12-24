"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from apps.app1.views import index  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route

    # Accounts URLs (like login, logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Including the URLs for your app (e.g., app1)
    path('app1/', include('apps.app1.urls')),

    # Add the home view for the root URL
    path('', index, name='home'),  # Redirect root URL to the index view
]

# For serving static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
