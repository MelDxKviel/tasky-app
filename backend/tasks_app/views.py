from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Task
from .serializers import (
    TaskRetrieveSerializer,
    TaskCreateSerializer,
    TaskUpdateSerializer,
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return Task.objects.filter(parent=None)
        else:
            queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return TaskUpdateSerializer
        elif self.action == 'create':
            return TaskCreateSerializer
        else:
            return TaskRetrieveSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != Task.Status.DONE:
            raise ValidationError("Нельзя удалить задачу в процессе выполнения")
        return super().destroy(request, *args, **kwargs)
    