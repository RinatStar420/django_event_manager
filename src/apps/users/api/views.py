from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    # serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]


    # Объявление метода для создания нового пользователя
    def post(self, request, *args, **kwargs):
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
