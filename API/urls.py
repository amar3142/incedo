from django.contrib import admin
from django.urls import path
from .views import Query

urlpatterns = [
    path('search/', Query.as_view()),
    ]
