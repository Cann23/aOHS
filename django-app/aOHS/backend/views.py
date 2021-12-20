from django.shortcuts import render

# Create your views here.
from django.views import View

from backend.models import Camera, Worker, Violation, Configuration


class CameraView(View):
    def get(self, request):
        return Camera.objects.all()


class WorkerView(View):
    def get(self, request):
        return Worker.objects.all()


class ViolationView(View):
    def get(self, request):
        return Violation.objects.all()


class ConfigurationView(View):
    def get(self, request):
        return Configuration.objects.all()


class Example(View):
    def get(self, request):
        return render(request, 'dashboard/index.html')

