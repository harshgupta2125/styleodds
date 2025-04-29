from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from accounts.views import profile_view, login_view, signup_view
from accounts.views import edit_profile_view

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout'),  
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/edit-profile/', edit_profile_view, name='edit_profile'),  # new

    
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]