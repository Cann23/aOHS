from django.contrib import admin
from django.urls import path

from dashboard.views import Example, Example2, WorkerView, ViolationView, Deneme

urlpatterns = [
    path('dashboard/', Example.as_view()),
    path('dashboard2/', Example2.as_view()),
    path('deneme/', Deneme.as_view()),
    path('dashboard/workers/', WorkerView.as_view()),
    path('dashboard/violation/', ViolationView.as_view()),
]
