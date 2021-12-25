from django.urls import path

from dashboard.views.camera_views import CameraView, CameraCreateView
from dashboard.views.configuration_views import ConfigurationView, ConfigurationCreateView
from dashboard.views.model_views import ModelView, ModelEditView
from dashboard.views.violation_views import ViolationView
from dashboard.views.worker_views import WorkerView, WorkerCreateView, WorkerEditView

urlpatterns = [
    path('dashboard/workers/', WorkerView.as_view()),
    path('dashboard/workers/add/', WorkerCreateView.as_view()),
    path('dashboard/workers/edit/<int:worker_id>/', WorkerEditView.as_view()),
    path('dashboard/violations/', ViolationView.as_view()),
    path('dashboard/models/', ModelView.as_view()),
    path('dashboard/models/edit/<int:model_id>/', ModelEditView.as_view()),
    path('dashboard/configurations/', ConfigurationView.as_view()),
    path('dashboard/configurations/add/', ConfigurationCreateView.as_view()),
    path('dashboard/cameras/', CameraView.as_view()),
    path('dashboard/cameras/add/', CameraCreateView.as_view()),
]
