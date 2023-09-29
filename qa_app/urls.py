from django.contrib import admin
from django.urls import path, include
from .views import index, submit_question
# app_name = "cnn_daily"
urlpatterns = [
    path('', index, name="index"),
    path('submit/', submit_question, name="submit_question"),

]