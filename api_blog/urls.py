from django.urls import path

from . import views


urlpatterns = [
    path('task-list/', views.taskList, name='task_list'),
    path('task-detail/<int:pk>/', views.taskDetail, name='task_detail'),
    path('task-create/', views.taskCreate, name='task_create'),
    path('task-update/<int:pk>/', views.taskUpdate, name='task_update'),
    path('task-delete/<int:pk>/', views.taskDelete, name='task_delete')
]