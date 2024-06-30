from datetime import datetime, UTC, date

from django.db import models
from django.core.exceptions import ValidationError


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'Назначена'
        IN_PROGRESS = 'Выполняется'
        PAUSED = 'Приостановлена'
        DONE = 'Завершена'

    title = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    executors = models.CharField(
        max_length=100,
        verbose_name='Список исполнителей',
        blank=True
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.NEW
    )

    complexity = models.IntegerField(
        verbose_name='Сложность'
    )

    execution_time = models.DurationField(
        verbose_name='Время выполнения',
        blank=True,
        null=True,
        default=None
    )

    end_date = models.DateTimeField(
        verbose_name='Дата завершения'
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name='subtasks'
    )

    def calculate_complexity(self):
        total_complexity = self.complexity
        for subtask in self.subtasks.all():
            subtask_complexity = subtask.calculate_complexity()
            total_complexity += subtask_complexity
        return total_complexity

    def __str__(self):
        return self.title

    def can_change_status(self, new_status):
        if self.status == self.Status.DONE:
            return False
        
        if new_status == self.Status.NEW and self.status != self.Status.NEW:
            return False

        if new_status == self.Status.DONE and self.status == self.Status.IN_PROGRESS:
            return True

        if new_status == self.Status.PAUSED and self.status != self.Status.IN_PROGRESS:
            return False

        if new_status == self.Status.DONE:
            for subtask in self.subtasks.all():
                if subtask.status != self.Status.DONE:
                    return False

        return True

    def change_status(self, new_status):
        if not self.can_change_status(new_status):
            raise ValidationError(f"Cannot change status from {self.status} to {new_status}")

        self.status = new_status
        self.save()

    def save(self, *args, **kwargs):
        if self.status == self.Status.DONE:
            self.execution_time = datetime.now(tz=UTC) - self.creation_date
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
