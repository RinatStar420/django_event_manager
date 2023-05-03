from django.db.models import F, Count
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_nested.viewsets import NestedViewSetMixin
from src.apps.base.api.mixins import SerializerPerActionMixin
from .serializers import EventSerializer, CreateEventSerializer, CreateDateSerializer, EventDateSerializer
from ..models import Event, EventDate
from django_filters import rest_framework as filters


class EventFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="eventdate__amount", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="eventdate__amount", lookup_expr='lte')

    class Meta:
        model = Event
        fields = ('min_price', 'max_price')


class EventViewSet(
    SerializerPerActionMixin,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Event.objects.all()
    filterset_class = EventFilter
    permission_classes = [AllowAny]

    action_serializers = {
        'default': EventSerializer,
        'create': CreateEventSerializer,

    }

    # def get_permissions(self):
    #     if self.action == 'create':
    #         self.permission_classes = [IsAuthenticated]
    #         return self.permission_classes
    #     else:
    #         self.permission_classes = [AllowAny]
    #     return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EventDateViewSet(
    SerializerPerActionMixin,
    ListModelMixin,
    CreateModelMixin,
    NestedViewSetMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = EventDate.objects.all()
    parent_lookup_kwargs = {'event_pk': 'event'}

    action_serializers = {
        'default': EventDateSerializer,
        'create': CreateDateSerializer,

    }

    @action(detail=True, methods=["get"], url_path=r'buy', permission_classes=[AllowAny])
    def buy(self, request, event_pk, pk):
        event_date = self.get_object()
        event_date.customers.add(request.user)
        serializer = self.get_serializer(event_date)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ('list', 'buy'):
            queryset = queryset.annotate(customers_number=Count('customers')).filter(customers_number__lt=F('tickets'))
        self.queryset = queryset
        return self.queryset

    def perform_create(self, serializer):
        event_pk = self.kwargs['event_pk']
        serializer.save(event=Event.objects.get(pk=event_pk))


