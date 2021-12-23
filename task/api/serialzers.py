from rest_framework import serializers
from ..models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'status', 'created_at']