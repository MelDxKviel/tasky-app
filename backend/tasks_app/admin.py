from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'creation_date']
    list_filter = ['status']
    search_fields = ['title']

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
