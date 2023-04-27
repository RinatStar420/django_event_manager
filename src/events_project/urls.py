from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter, NestedMixin
from apps.events.api.views import EventViewSet, EventDateSet, CreateDataViewSet, CreateEventViewSet

router = SimpleRouter()
router.register('events', EventViewSet)
router.register('create_event', CreateEventViewSet , basename='Event')
nested_event_router = NestedSimpleRouter(router, 'events', lookup='event')
nested_event_router.register('dates', EventDateSet)
nested_event_router.register('create_date', CreateDataViewSet, basename='Eventdate')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(nested_event_router.urls)),
    path('api/token/', include('apps.api_auth.api.urls')),
]
