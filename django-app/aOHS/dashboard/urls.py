from django.contrib import admin
from django.urls import path

from dashboard.views import Example

urlpatterns = [
    path('dashboard/', Example.as_view()),
]
