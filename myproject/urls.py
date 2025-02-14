"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('myapp.urls')),  
    path('accounts/', include('social_django.urls', namespace='social')),
    path('images/', views.image_list, name='image_list'),
    path('images/<str:image_id>/', views.get_image, name='get_image'),
    path('allimages/', views.display_images, name='display_images'),
    #path('accounts/login/', LoginView.as_view(), name='account_login'),
    
]
