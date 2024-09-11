from rest_framework import serializers

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
    status = StatusSerializer()
    priority = PrioritySerializer()