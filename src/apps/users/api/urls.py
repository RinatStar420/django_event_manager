from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('registr/', UserCreateView.as_view(), name='registr'),
]
