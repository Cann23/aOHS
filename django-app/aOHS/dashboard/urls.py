from django.urls import path

from dashboard.views.camera_views import CameraView, CameraCreateView, CameraEditView, CameraDeleteView
from dashboard.views.camera_views import index, ImageView, Home
from dashboard.views.configuration_views import ConfigurationView, ConfigurationCreateView, ConfigurationEditView, \
    ConfigurationDeleteView
from dashboard.views.dashboard_views import DashboardView
from dashboard.views.model_views import ModelView, ModelEditView, ModelDeleteView
from dashboard.views.profile_views import ProfileView
from dashboard.views.statistic_views import StatisticView
from dashboard.views.stream_views import StreamView
from dashboard.views.violation_views import ViolationView, ViolationCreateView, ViolationEditView, ViolationDeleteView,\
    ViolationWorkerView, ViolationCaptureView, ViolationDailyView, ViolationDailySelectView
from dashboard.views.worker_views import WorkerView, WorkerCreateView, WorkerEditView, WorkerDeleteView
from dashboard.views.specialist_views import SpecialistView, SpecialistCreateView, SpecialistEditView, \
    SpecialistDeleteView, SpecialistCameraView

urlpatterns = [
    path('', ViolationDailyView.as_view()),
    path('workers/', WorkerView.as_view()),
    path('workers/add/', WorkerCreateView.as_view()),
    path('workers/edit/<int:worker_id>/', WorkerEditView.as_view()),
    path('workers/delete/<int:worker_id>/', WorkerDeleteView.as_view()),

    path('specialists/', SpecialistView.as_view()),
    path('specialists/add/', SpecialistCreateView.as_view()),
    path('specialists/cameras/<int:specialist_id>/', SpecialistCameraView.as_view()),
    path('specialists/edit/<int:specialist_id>/', SpecialistEditView.as_view()),
    path('specialists/delete/<int:specialist_id>/', SpecialistDeleteView.as_view()),

    path('violations/', ViolationView.as_view()),
    path('violations/<int:violation_id>/', ViolationCaptureView.as_view()),
    path('violations/worker/<int:worker_id>/', ViolationWorkerView.as_view()),
    path('violations/add/', ViolationCreateView.as_view()),
    path('violations/edit/<int:violation_id>/', ViolationEditView.as_view()),
    path('violations/delete/<int:violation_id>/', ViolationDeleteView.as_view()),
    path('violations/daily/',ViolationDailyView.as_view()),
    path('violations/daily/select/<int:date>/',ViolationDailySelectView.as_view()),

    path('models/', ModelView.as_view()),
    path('models/edit/<int:model_id>/', ModelEditView.as_view()),
    path('models/delete/<int:model_id>/', ModelDeleteView.as_view()),

    path('configurations/', ConfigurationView.as_view(), name='configurationsList'),
    path('configurations/add/', ConfigurationCreateView.as_view()),
    path('configurations/edit/<int:configuration_id>/', ConfigurationEditView.as_view()),
    path('configurations/delete/<int:configuration_id>/', ConfigurationDeleteView.as_view()),

    path('cameras/', CameraView.as_view()),
    path('cameras/add/', CameraCreateView.as_view()),
    path('cameras/edit/<int:camera_id>/', CameraEditView.as_view()),
    path('cameras/delete/<int:camera_id>/', CameraDeleteView.as_view()),

    path('statistics/', StatisticView.as_view()),
    path('streams/', StreamView.as_view()),
    path('video/', index),
    path('img/x/<int:id>', ImageView.as_view()),
    path('img/', Home.as_view()),
    path('profile/', ProfileView.as_view()),
]
