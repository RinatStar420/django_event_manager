from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView



class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer