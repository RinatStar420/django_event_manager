from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter, NestedMixin
from src.apps.events.api.views import EventViewSet, EventDateViewSet

router = SimpleRouter()
router.register('events', EventViewSet)
nested_event_router = NestedSimpleRouter(router, 'events', lookup='event')
nested_event_router.register('dates', EventDateViewSet)
# nested_event_router.register('create_date', CreateDataViewSet, basename='Eventdate')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(nested_event_router.urls)),
    path('api/token/', include('src.apps.api_auth.api.urls')),
]
