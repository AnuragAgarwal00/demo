from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Activity
from .forms import TaskCreateForm

class TaskListView(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'task/list.html'


class TaskCreateView(CreateView, LoginRequiredMixin):
    form_class = TaskCreateForm
    # fields = ['title', 'deadline']
    template_name = 'task/create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView, LoginRequiredMixin):
    model = Task
    fields = ['status']
    template_name = 'task/update.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.status = Task.COMPLETE
        object.save()
        super().form_valid(form)


class TaskDeleteView(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('task_list')

class ActivityLogs(ListView):
    model = Activity
    template_name = 'activity/list.html'




# Create your views here.
