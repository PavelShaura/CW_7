import pytest


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    url = '/goals/goal_category/'
    response = api_client.get(url)
    assert response.status_code == 401


