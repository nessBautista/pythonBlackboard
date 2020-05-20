from django.urls import path
from .views import (
    TagApiDetail,
    TagApiList,
    StartupAPIDetail,
    StartupAPIList,
)

urlpatterns = [
    path("tag/", TagApiList.as_view(), name="api-tag-list"),
    path("tag/<str:slug>/", TagApiDetail.as_view(), name="api-tag-detail"),
    path("startup/", StartupAPIList.as_view(), name="api-startup-list"),
    path("startup/<str:slug>/", StartupAPIDetail.as_view(), name="api-startup-detail"),
]
