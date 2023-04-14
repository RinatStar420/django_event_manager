from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .api.serializers import MyTokenObtainPairSerializer
from .models import Event


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class EventAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lst = Event.objects.all().values()
        return Response({'title': list(lst)})


