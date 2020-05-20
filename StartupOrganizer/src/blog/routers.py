from django.urls import path

from .views import PostAPIDetail, PostAPIList

urlpatterns = [
    path("blog/", PostAPIList.as_view(), name="api-post-list"),
    path("blog/<int:year>/<str:slug>", PostAPIDetail.as_view(), name="api-post-detail"),
]
