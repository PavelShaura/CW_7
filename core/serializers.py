from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class PasswordField(serializers.CharField):

    def __init__(self, **kwargs):
        kwargs['style'] = {'input_type': 'password'}
        kwargs.setdefault('write_only', True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class CreateUserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password_repeat = PasswordField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_repeat']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError('Passwords must match')
        return attrs

    def create(self, validated_data):
        del validated_data['password_repeat']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError(["User not exists"])
        return value


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = PasswordField(required=True)
    new_password = PasswordField(required=True)

    def validate(self, attrs):
        if not self.instance.check_password(attrs['old_password']):
            raise ValidationError({'old_password': 'field is incorrect'})
        return attrs

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['new_password'])
        instance.save(update_fields=('password',))
        return instance

    def create(self, validated_data):
        raise NotImplementedError
