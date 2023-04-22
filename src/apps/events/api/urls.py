from django.urls import path
from .views import EventAPIView, CreateDateView, CreateEvent

urlpatterns = [
    path('', EventAPIView.as_view()),
    path('<int:pk>/create_date/', CreateDateView.as_view()),
    path('create_event/', CreateEvent.as_view()),
]
