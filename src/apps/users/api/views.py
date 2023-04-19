from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer

