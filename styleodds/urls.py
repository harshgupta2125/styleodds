"""
URL configuration for styleodds project.

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
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('shop', views.shop, name="shop"),
    path('view_details', views.view_details, name="view_details"),
    path('about', views.about, name="about"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name='checkout'),
    path('base', views.base, name='base'),
    path('vintage_archive', views.vintage_archive, name='vintage_archive'),
    path('style_boards', views.style_boards, name='style_boards'),  
    
    path('accounts/', include('accounts.urls')),
    
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success_view, name='success'),
    
    
    
    path("__reload__/", include("django_browser_reload.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
