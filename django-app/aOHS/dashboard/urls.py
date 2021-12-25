from django.contrib import admin
from django.urls import path

from dashboard.views import Example, Example2, WorkerView, ViolationView, ModelView, WorkerCreateView, \
    ConfigurationView, CameraView, CameraCreateView, ConfigurationCreateView

urlpatterns = [
    path('dashboard/', Example.as_view()),
    path('dashboard2/', Example2.as_view()),
    path('dashboard/workers/', WorkerView.as_view()),
    path('dashboard/workers/add/', WorkerCreateView.as_view()),
    path('dashboard/violations/', ViolationView.as_view()),
    path('dashboard/models/', ModelView.as_view()),
    path('dashboard/configurations/', ConfigurationView.as_view()),
    path('dashboard/configurations/add/', ConfigurationCreateView.as_view()),
    path('dashboard/cameras/', CameraView.as_view()),
    path('dashboard/cameras/add/', CameraCreateView.as_view()),
]
