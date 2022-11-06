from django.urls import path
import bot.views as views

urlpatterns = [
    path("verify", views.TgUserUpdateView.as_view()),
]