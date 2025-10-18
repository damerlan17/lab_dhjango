from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path("post_list/", views.post_list)
]