from rest_framework import serializers
from ..models import Event, EventDate
from apps.users.models import User


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

    def get_price(self, obj):
        return {'currency': obj.currency, 'amount': obj.amount}

    class Meta:
        model = EventDate
        fields = ('pk', 'start', 'end', 'price', 'tickets')


class EventSerializer(serializers.ModelSerializer):
    event_dates = EventDateSerializer(many=True, source='dates')
    author = UserSerializer()

    class Meta:
        model = Event
        fields = ('pk', 'title', 'author', 'description', 'location', 'event_dates')


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'location')
