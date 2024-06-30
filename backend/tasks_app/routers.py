from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

tasks_router = DefaultRouter()
tasks_router.register('tasks', TaskViewSet)
