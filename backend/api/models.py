"""Модуль, содержащий модели данных приложения."""

from django.db import models


class Task(models.Model):
    """Модель задачи.

    Attributes:
        title (str): Заголовок задачи
        description (str): Описание задачи
        completed (bool): Статус выполнения задачи
    """

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
