from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('GET/task/', views.getTask, name="get.task"),
    path('GET/task/<int:id>', views.getdescription, name="get.task.description"),
    path('POST/tasks/', views.addtask, name="post.task"),
    path('DELETE/tasks/<int:id>', views.deletetask, name="delete.task"),
    path('PUT/tasks/<int:id>', views.updatetask, name="put.update.task"),
]
