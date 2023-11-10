from src.apps.events.models import Event
import pytest


@pytest.fixture
def get_url():
    return '/api/v1/events/'

@pytest.mark.django_db
def test_event(client, get_url):
    response = client.get(get_url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_add_event(user, client, get_url):  # добавить фикстуру создания юзера
    client.force_authenticate(user)
    payload = dict(title='random event',
                   description='this is description to random event',
                   location='Randomvill',
                   )
    response = client.post(get_url, payload)

    assert response.status_code == 201

    assert Event.objects.filter(author=user, pk=response.data['pk']).exists()


@pytest.mark.django_db
def test_buy_ticket(client):
    response = client.get('/api/v1/events/1/dates/1/buy/')


    assert response.status_code == 401  #TODO создать файл с рецептами в приложении евенртс,
                                        # в нем создать два рецепта евент и дата, которы будет связан с рецептом евента,
                                        # в самом тесте возможно надо будет создать только дату, далее беру айди из созданной даты и евента, евент скорее вмего беру из даты

                                        # revers из resta есть команда show_urls (нужен кваргс 1 евент пк, 2 просто пк)
