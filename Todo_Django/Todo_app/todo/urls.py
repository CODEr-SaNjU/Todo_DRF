from django.urls import path, include
from . import views


urlpatterns = [
    path('todo-list/', views.TodoView, name='Todo-view'),
    path('todo-create/', views.TodoCreate, name='Todo-create'),
    path('todo-details/<str:pk>/', views.TodoDetails, name='Todo-details'),
    path('todo-update/<str:pk>/', views.TodoUpdate, name='Todo-update'),
    path('todo-delete/<str:pk>/', views.TodoDelete, name='Todo-delete'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
