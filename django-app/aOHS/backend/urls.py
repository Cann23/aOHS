from django.urls import path

from backend.views import IndexView

urlpatterns = [
    # path('dashboard/', Example.as_view()),
    path('deneme/', IndexView.as_view()),
]
