from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.enums import Choices



class Activity(models.Model):
    COMMENTED = 'CM'
    COMPLETED ='C'
    DELETED = 'D'
    CREATED = 'CRE'
    ACTIVITY_CHOICES = (
        ('commented', COMMENTED),
        ('completed', COMPLETED),
        ('deleted', DELETED),
        ('created', CREATED),
    )
    action = models.CharField(max_length=250, choices=ACTIVITY_CHOICES)
    description = models.TextField()
    action_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    COMPLETE = 'C'
    PENDING = 'P'
    DELIVERED = 'D'
     
    status_choices = (
        ('complete', COMPLETE),
        ('pending', PENDING),
        ('delivered', DELIVERED)
    )
    
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='task_activity', null=True, blank=True)
    title = models.CharField(max_length=250)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=25, choices=status_choices, default=PENDING)
    created_at = models.DateField(auto_now=True)
    completed_on = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title




