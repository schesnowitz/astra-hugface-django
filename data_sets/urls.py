from django.contrib import admin
from django.urls import path, include
from .views import index, show, create, create_data_set
app_name = "data_set"
urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('create_data_set/', create_data_set, name="create_data_set"),
    path('show/<int:pk>/', show, name="show"),


]