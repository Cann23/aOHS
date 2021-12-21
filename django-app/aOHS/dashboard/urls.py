from django.contrib import admin
from django.urls import path

from dashboard.views import Example, Example2, WorkerView, ViolationView, ModelView, Deneme, ConfigurationView

urlpatterns = [
    path('dashboard/', Example.as_view()),
    path('dashboard2/', Example2.as_view()),
    path('dashboard/workers/', WorkerView.as_view()),
    path('dashboard/violations/', ViolationView.as_view()),
    path('dashboard/models/', ModelView.as_view()),
    path('dasboard/configurations/', ConfigurationView.as_view()),
]
