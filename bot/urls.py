from django.urls import path
from bot import views

urlpatterns = [
    path('verify', views.TelegramVerificationView.as_view(), name='telegram_verify_user'),
]