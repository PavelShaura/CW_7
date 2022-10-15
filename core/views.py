from django.contrib.auth import login, logout, authenticate
from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from core.models import User
from core.serializers import CreateUserSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # validate request data
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(data={'password': ['Invalid password']}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
