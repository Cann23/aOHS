from django.urls import path

from backend.views import IndexView

urlpatterns = [
    # path('dashboard/', Example.as_view()),
    path('', IndexView.as_view()),
]
