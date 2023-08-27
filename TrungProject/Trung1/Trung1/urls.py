from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls1/", include("polls1.urls")),
    path("admin/", admin.site.urls),
]