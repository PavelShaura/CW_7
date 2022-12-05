import json
import pytest

from goals.models import Board
from goals.serializers import BoardListSerializer, BoardCreateSerializer, BoardSerializer
from tests.factories import BoardFactory

pytestmark = pytest.mark.django_db


class TestBoard:

    endpoint = '/goals/board/'
    endpoint_list = '/goals/board/list'
    endpoint_create = '/goals/board/create'

    def test_list(self, api_client, user_client):

        boards = BoardFactory.create_batch(10)

        expected_json = {
            "count": 10,
            "next": None,
            "previous": None,
            "results": BoardListSerializer(boards, many=True).data
        }

        response = api_client().get(
            self.endpoint_list,
            HTTP_AUTHORIZATION=user_client
        )

        assert response.status_code == 200
        assert response.data == expected_json

    def test_create(self, api_client, user_client):

        boards = BoardFactory.create_batch(10)

        expected_json = {
            "count": 10,
            "next": None,
            "previous": None,
            "results": BoardCreateSerializer(boards, many=True).data
        }

        response = api_client().post(
            self.endpoint_create,
            data=expected_json,
            format='json',
            HTTP_AUTHORIZATION=user_client
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client, user_client, board):

        boards = BoardFactory.create_batch(1)

        expected_json = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": BoardSerializer(boards, many=True).data
        }

        url = f'{self.endpoint}{board.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_delete(self, api_client, user_client, board):
        url = f'{self.endpoint}{board.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Board.objects.all().count() == 0