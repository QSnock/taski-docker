"""Модуль настройки административной панели Django."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройки отображения модели Task в админ-панели."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
