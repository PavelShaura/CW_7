import pytest
from rest_framework.test import APIClient

from goals.models import Board


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser',
        password='1234567'
    )


@pytest.fixture
def user_client(user, client):
    client.force_login(user)
    return client


@pytest.fixture
def board():
    return Board.objects.create(
        title='TestBoard'
    )


@pytest.fixture
def api_client():
    return APIClient
