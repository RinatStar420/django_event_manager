from django.urls import path
from .views import EventViewSet,CreateEvent #CreateDateView,

urlpatterns = [
    # path('', EventViewSet.as_view()),
    # path('<int:pk>/create_date/', CreateDateView.as_view()),
    # path('create_event/', CreateEvent.as_view()),
]
