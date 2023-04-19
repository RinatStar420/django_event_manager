from rest_framework import serializers
from ..models import Event, EventDate
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ('start', 'end',)

class EventSerializer(serializers.ModelSerializer):
    # event_dates = EventDateSerializer()
    dates = EventDateSerializer(many=True, source='eventdate_set')
    author = UserSerializer()
    class Meta:
        model = Event
        fields = ('title', 'author', 'description', 'location', 'dates',)