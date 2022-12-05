import json
import pytest

from goals.models import Goal
from goals.serializers import GoalSerializer, GoalCreateSerializer

from tests.factories import GoalFactory

pytestmark = pytest.mark.django_db


class TestGoal:

    endpoint = '/goals/goal/'
    endpoint_list = '/goals/goal/list'
    endpoint_create = '/goals/goal/create'

    def test_list(self, api_client, user_client):

        goals = GoalFactory.create_batch(10)

        expected_json = {
            "count": 10,
            "next": None,
            "previous": None,
            "results": GoalSerializer(goals, many=True).data
        }

        response = api_client().get(
            self.endpoint_list,
            HTTP_AUTHORIZATION=user_client
        )

        assert response.status_code == 200
        assert response.data == expected_json

    def test_create(self, api_client, user_client):

        goals = GoalFactory.create_batch(10)

        expected_json = {
            "count": 10,
            "next": None,
            "previous": None,
            "results": GoalCreateSerializer(goals, many=True).data
        }

        response = api_client().post(
            self.endpoint_create,
            data=expected_json,
            format='json',
            HTTP_AUTHORIZATION=user_client
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client, user_client, goal):

        goals = GoalFactory.create_batch(1)

        expected_json = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": GoalSerializer(goals, many=True).data
        }

        url = f'{self.endpoint}{goal.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_delete(self, api_client, user_client, goal):
        url = f'{self.endpoint}{goal.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Goal.objects.all().count() == 0