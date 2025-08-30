# ShadowApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.shadow_statement, name="shadow"),
]
