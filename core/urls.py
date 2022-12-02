from django.urls import path
from .views import SignUpView, LoginView, UserRetrieveUpdateView, PasswordUpdateView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='user_create'),
    path('login', LoginView.as_view(), name='core_login'),
    path('profile', UserRetrieveUpdateView.as_view()),
    path('update_password', PasswordUpdateView.as_view())
]
