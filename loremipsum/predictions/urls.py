from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('predecir/', views.post_fastapi_data, name="predict"),
]