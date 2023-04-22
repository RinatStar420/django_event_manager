from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import EventSerializer, CreateEventSerializer, CreateDateSerializer
from ..models import Event, EventDate
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


# хуйня какая-то получается
# class EventFilter(filters.FilterSet):
#     min_price = filters.NumberFilter(field_name="amount", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="amount", lookup_expr='lte')
#
#     class Meta:
#         model = EventDate
#         fields = ('amount',)
#

# Тут был класс вью, я удалил
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = EventFilter

class EventAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CreateDateView(CreateAPIView):
    serializer_class = CreateDateSerializer


class CreateEvent(CreateAPIView):
    serializer_class = CreateEventSerializer
