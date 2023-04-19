from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventlist/', include('apps.events.api.urls')),
    path('api/v1/', include('apps.users.api.urls')),
    path('api/token/', include('apps.api_auth.api.urls')),
]
