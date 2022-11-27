from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Todo_new, name='Post_new'),
    path('Todolist',views.Todo_list, name='Todolist'),
    path('Todo_del/<int:pk>/delete/',views.Todo_delete,name='Todo_delete'),
    path('Todo_update/<int:pk>/update/',views.Todo_update, name='Todo_update'),
]  
