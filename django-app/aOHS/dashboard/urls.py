from django.urls import path

from dashboard.views import Example, Example2, WorkerView, ViolationView, ModelView

urlpatterns = [
    path('dashboard/', Example.as_view()),
    path('dashboard2/', Example2.as_view()),
    path('dashboard/workers/', WorkerView.as_view()),
    path('dashboard/violations/', ViolationView.as_view()),
    path('dashboard/models/', ModelView.as_view()),
]
