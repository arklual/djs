from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    path("admin/", views.admin, name="admin"),
    path("clear/", views.clear, name="clear"),
]