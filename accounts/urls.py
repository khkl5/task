from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ الرئيسية
    path('register/', views.register, name='register'),
    path('validate-username/', views.validate_username, name='validate_username'),
    path('validate-email/', views.validate_email, name='validate_email'),
    path('validate-phone/', views.validate_phone, name='validate_phone'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('users/', views.user_list, name='user_list'),
]
