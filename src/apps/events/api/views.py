from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_nested.viewsets import NestedViewSetMixin

from .serializers import EventSerializer, CreateEventSerializer, CreateDateSerializer, EventDateSerializer
from ..models import Event, EventDate
from django_filters import rest_framework as filters


class EventFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="eventdate__amount", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="eventdate__amount", lookup_expr='lte')

    class Meta:
        model = Event
        fields = ('min_price', 'max_price')


# class EventAPIView(ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     filterset_class = EventFilter


class EventViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter


class EventDateSet(ListModelMixin,
                   NestedViewSetMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    queryset = EventDate.objects.all()
    parent_lookup_kwargs = {'event_pk': 'event'}  #event__pk
    serializer_class = EventDateSerializer


# class CreateDateView(CreateAPIView):
#     serializer_class = CreateDateSerializer
#
#
#     def create(self, request, pk):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(event=Event.objects.get(pk=pk))
#         data = serializer.data
#         return Response(data, status=status.HTTP_201_CREATED)


# class CreateEvent(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CreateEventSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save(author=request.user)
#         data = serializer.data
#         return Response(data, status=status.HTTP_201_CREATED)


class CreateEventViewSet(CreateModelMixin,
                        GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateEventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class CreateDataViewSet(CreateModelMixin,
                        GenericViewSet):

    serializer_class = CreateDateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(event=serializer) # выяснить, что сюда
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
