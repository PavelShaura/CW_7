import pytest


@pytest.mark.django_db
def test_authorized_request(api_client, get_or_create_token):
    url = '/goals/goal_category/'
    token = get_or_create_token()
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = api_client.get(url)
    assert response.status_code == 200
