from rest_framework import serializers
from ..models import User


class UserCreateSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    repeated_password = serializers.CharField()

    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = (
            'pk',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'repeated_password'
        )

    def validate(self, attrs):
        repeated_password = attrs.pop('repeated_password')
        if attrs['password'] != repeated_password:
            raise serializers.ValidationError({'repeated_password': 'Пароли не совпадают'})

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
