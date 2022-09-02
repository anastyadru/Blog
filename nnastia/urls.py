from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.nnastia_index, name="nnastia_index"),
    path("<int:pk>/",views.nnastia_detail, name="nnastia_detail"),
]