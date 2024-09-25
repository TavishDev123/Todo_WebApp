from django.urls import path
from . import views
from .views import Home, todo_list

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'), 
    path('todos/', views.todo_list, name='todos'),
    path('todos/add/', views.add_todo, name='todo-add'),
    path('todos/<int:todo_id>/edit/', views.edit_todo, name='edit_todo'), 
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='todo-delete'),
]
