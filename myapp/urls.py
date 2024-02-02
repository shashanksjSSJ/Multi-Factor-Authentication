from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
     path('otp/', views.otp_pin_view, name='otp_pin'),
      path('register/', views.register_view, name='register'),
      path('success/', views.success, name='success'),
]
