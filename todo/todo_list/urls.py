from django.urls import path
from . import views

app_name = "todo_list"

urlpatterns = [
    path("", views.home, name="home"),
    path("tags/", views.tag_list, name="tag_list"),
    path("add_task/", views.add_task, name="add_task"),
    path("add_tag/", views.add_tag, name="add_tag"),
    path("update_task/<int:pk>/", views.update_task, name="update_task"),
    path("update_tag/<int:pk>/", views.update_tag, name="update_tag"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
    path("delete_tag/<int:pk>/", views.delete_tag, name="delete_tag"),
    path("toggle_task_status/<int:pk>/", views.toggle_task_status, name="toggle_task_status"),
]
