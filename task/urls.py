from django.urls import path, include

from . import views

urlpatterns = [
    path("list/", views.TaskListView.as_view(), name="task_list"),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path("mark-completed/<pk>/", views.TaskUpdateView.as_view(), name="mark_task_complete"),
    path('delete/<pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('activity/', views.ActivityLogs.as_view(), name='task_activity')
]
