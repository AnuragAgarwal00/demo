from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Task, Activity
 
 
@receiver(post_save, sender=Task)
def create_activity_post_save(sender, instance, created, **kwargs):
    if created:
        activity = Activity.objects.create(
            action=Activity.CREATED, 
            description=f"{instance.user.first_name} created the task {instance.title}")
        instance.activity = activity
        instance.save()
        
  
@receiver(pre_delete, sender=Task)
def create_activity_post_delete(sender, **kwargs):
    activity = Activity.objects.create(
            action=Activity.DELETED, 
            description=f"{kwargs['instance'].user.first_name} deleted the task {kwargs['instance'].title}")