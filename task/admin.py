from django.contrib import admin
from django.db.models import fields
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['user', 'title', 'deadline']

# Register your models here.
