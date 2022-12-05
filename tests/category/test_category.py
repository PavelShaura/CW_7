import json
import pytest

from goals.models import Category
from goals.serializers import CategorySerializer, CategoryCreateSerializer
from tests.factories import CategoryFactory

pytestmark = pytest.mark.django_db


class TestCategory:

    endpoint = '/goals/goal_category/'
    endpoint_list = '/goals/goal_category/list'
    endpoint_create = '/goals/goal_category/create'

    def test_list(self, api_client, user_client):

        categories = CategoryFactory.create_batch(10)

        expected_json = {
            "count": 10,
            "next": None,
            "previous": None,
            "results": CategorySerializer(categories, many=True).data
        }

        response = api_client().get(
            self.endpoint_list,
            HTTP_AUTHORIZATION=user_client
        )

        assert response.status_code == 200
        assert response.data == expected_json

    def test_create(self, api_client, user_client):

        categories = CategoryFactory.create_batch(10)

        expected_json = {
            "count": 10,
            "next": None,
            "previous": None,
            "results": CategoryCreateSerializer(categories, many=True).data
        }

        response = api_client().post(
            self.endpoint_create,
            data=expected_json,
            format='json',
            HTTP_AUTHORIZATION=user_client
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client, user_client, category):

        categories = CategoryFactory.create_batch(1)

        expected_json = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": CategorySerializer(categories, many=True).data
        }

        url = f'{self.endpoint}{category.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_delete(self, api_client, user_client, category):
        url = f'{self.endpoint}{category.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Category.objects.all().count() == 0