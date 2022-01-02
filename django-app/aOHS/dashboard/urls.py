from django.urls import path

from dashboard.views.camera_views import CameraView, CameraCreateView, CameraEditView
from dashboard.views.configuration_views import ConfigurationView, ConfigurationCreateView, ConfigurationEditView
from dashboard.views.model_views import ModelView, ModelEditView
from dashboard.views.statistic_views import StatisticView
from dashboard.views.violation_views import ViolationView, ViolationCreateView, ViolationEditView
from dashboard.views.worker_views import WorkerView, WorkerCreateView, WorkerEditView
from dashboard.views.camera_views import index

urlpatterns = [
    path('dashboard/workers/', WorkerView.as_view()),
    path('dashboard/workers/add/', WorkerCreateView.as_view()),
    path('dashboard/workers/edit/<int:worker_id>/', WorkerEditView.as_view()),
    path('dashboard/violations/', ViolationView.as_view()),
    path('dashboard/violations/add/', ViolationCreateView.as_view()),
    path('dashboard/violations/edit/<int:violation_id>/', ViolationEditView.as_view()),
    path('dashboard/models/', ModelView.as_view()),
    path('dashboard/models/edit/<int:model_id>/', ModelEditView.as_view()),
    path('dashboard/configurations/', ConfigurationView.as_view()),
    path('dashboard/configurations/add/', ConfigurationCreateView.as_view()),
    path('dashboard/configurations/edit/<int:configuration_id>/', ConfigurationEditView.as_view()),
    path('dashboard/cameras/', CameraView.as_view()),
    path('dashboard/cameras/add/', CameraCreateView.as_view()),
    path('dashboard/cameras/edit/<int:camera_id>/', CameraEditView.as_view()),
    path('dashboard/statistics/', StatisticView.as_view()),
    path('video/', index),
]
