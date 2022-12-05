import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_user_detail(client, create_user):
    user = create_user(username='someone')
    url = reverse('user_create', kwargs={'pk': user.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'someone' in response.content
