from rest_framework import serializers
from ..models import Event, EventDate
from src.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class CreateDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ('event', 'currency', 'amount', 'tickets', 'start', 'end',)
        extra_kwargs = {'event': {'read_only': True}}


class EventDateSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    tickets_left = serializers.SerializerMethodField()

    def get_tickets_left(self, obj):
        return obj.tickets - obj.customers.count()

    # annotate(customers_number=Count('customers')).filter(customers_number__lt=F('tickets'))

    def get_price(self, obj):
        return {'currency': obj.currency, 'amount': obj.amount}


    class Meta:
        model = EventDate
        fields = ('pk', 'start', 'end', 'price', 'tickets', 'tickets_left',)


class EventSerializer(serializers.ModelSerializer):
    event_dates = EventDateSerializer(many=True, source='dates')
    author = UserSerializer()

    class Meta:
        model = Event
        fields = ('pk', 'title', 'author', 'description', 'location', 'event_dates')


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'author','description', 'location')
