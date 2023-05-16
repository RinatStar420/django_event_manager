from rest_framework.test import APIClient
import pytest

client = APIClient()


@pytest.mark.django_db
def test_event():
    response = client.get('/api/v1/events/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_add_event():
    payload = dict(title='random event',
                   author='user1',
                   description='this is description to random event',
                   location='Randomvill',
                   )
    response = client.post('/api/v1/events/', payload)

    assert response.status_code >= 400


@pytest.mark.django_db
def test_buy_ticket():
    response = client.get('/api/v1/events/1/dates/1/buy/')

    assert response.status_code == 401
