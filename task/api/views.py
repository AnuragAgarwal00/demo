from .serialzers import TaskSerializers
from rest_framework.viewsets import ModelViewSet
from ..models import Task

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    ordering_fields = ['created_at']