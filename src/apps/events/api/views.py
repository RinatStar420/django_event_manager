from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Event


class EventAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lst = Event.objects.all().values()
        return Response({'title': list(lst)})
