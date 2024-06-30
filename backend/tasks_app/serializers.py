from rest_framework import serializers
from django.utils.duration import duration_string

from .models import Task


class TaskRetrieveSerializer(serializers.ModelSerializer):
    total_complexity = serializers.IntegerField(
        source='calculate_complexity', read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'creation_date',
            'end_date',
            'executors',
            'execution_time',
            'status',
            'complexity',
            'total_complexity',
            'subtasks'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subtasks'] = TaskRetrieveSerializer(
            instance.subtasks.all(), many=True).data
        if instance.execution_time:
            representation['execution_time'] = duration_string(
                instance.execution_time)
        return representation


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'creation_date',
            'end_date',
            'executors',
            'execution_time',
            'status',
            'complexity',
            'subtasks',
            'parent'
        )
        read_only_fields = (
            'id',
            'creation_date',
            'execution_time',
            'status',
            'subtasks'
        )

    def create(self, validated_data):
        parent_task = validated_data.get('parent')
        if parent_task and parent_task.status == Task.Status.DONE:
            raise serializers.ValidationError(
                "Родительская задача уже завершена")
        return super().create(validated_data)


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'execution_time')

    def validate(self, data):
        instance = self.instance
        if instance.status == Task.Status.DONE:
            raise serializers.ValidationError({
                'status': [f"Нельзя изменить завершенную задачу"]})
        new_status = data.get('status', instance.status)
        if not instance.can_change_status(new_status):
            raise serializers.ValidationError({
                'status': [f"Нельзя изменить статус задачи с {instance.status} на {new_status}"]})
        return super().validate(data)

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)
        instance.change_status(new_status)

        return super().update(instance, validated_data)
