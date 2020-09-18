from django.urls import path
from . import views

urlpatterns = [
    #path("", views.apiOverview, name="api-overview"),
    path("task-list/", views.taskList, name="task-list"),
    path("task-detail/", views.taskDetail, name="task-detail"),
    path("shopfront/", views.shopfront, name="shopfront"),
]
