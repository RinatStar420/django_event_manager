from rest_framework import serializers
from ..models import Event, EventDate
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ( 'currency', 'amount',)


class CreateDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ('event', 'currency', 'amount', 'tickets', 'start', 'end',)


class EventDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventDate
        fields = ('start', 'end', )



class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title','author', 'description', 'location')


class EventSerializer(serializers.ModelSerializer):
    event_dates = EventDateSerializer(many=True, source='eventdate_set')
    author = UserSerializer()

    class Meta:
        model = Event
        fields = ('title', 'author', 'description', 'location', 'event_dates')
