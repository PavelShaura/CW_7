import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        id=0,
        username="string",
        first_name="string",
        last_name="string",
        email="user@example.com",
        password="string"
    )
    response = client.get(
        "/core/signup/",
        payload,
        format="json",
    )
    data = response.data

    assert data == payload
    assert "password" not in data
