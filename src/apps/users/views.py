from .api.serializers import UserRegistrSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User


class RegistrUserView(CreateAPIView):
    # Добавление в queryset
    queryset = User.objects.all()
    # Добавление serializer UserRegistrSerializer
    serializer_class = UserRegistrSerializer
    # Добавление прав доступа
    permission_classes = [AllowAny]

    # Объявление метода для создания нового пользователя
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        # Создаём список data
        data = {}
        # Проверка данных на валидность
        if serializer.is_valid():
            # Сохранение нового пользователя
            serializer.save()
            # Добавление в список значение ответа True
            data['response'] = True
            # Возврат что всё ок
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
