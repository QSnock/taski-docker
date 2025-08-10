"""Модуль сериализации данных для API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Task."""

    class Meta:
        """Мета-класс для настройки сериализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
