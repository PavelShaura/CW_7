import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_login_view(client, create_user, test_password):
    user = create_user()
    url = reverse('core_login')
    client.login(
        username=user.username, password=test_password
    )
    response = client.get(url)
    assert response.status_code == 200
