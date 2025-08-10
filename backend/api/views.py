"""Модуль представлений API для работы с задачами."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """Представление для работы с задачами.

    Поддерживает все стандартные операции CRUD через API.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Удаляет задачу и возвращает её данные.

        Returns:
            Response: Удалённая задача и статус 200
        """
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
