from rest_framework import serializers

from app.serializers.project_serializer import ProjectSerializer


class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    label = serializers.CharField()

class PrioritySerializer(serializers.Serializer):
    label = serializers.CharField()
    level = serializers.IntegerField(required=False, read_only=True)


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    status = StatusSerializer(read_only=True)
    priority = PrioritySerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

class TaskCreationSerializer(TaskSerializer):
    priority_id = serializers.IntegerField(write_only=True)
    status_id = serializers.IntegerField(write_only=True)
    project_id = serializers.IntegerField(write_only=True)

