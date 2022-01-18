import requests
from django.shortcuts import render, redirect

from django.views import View

from backend.models import Configuration, Camera, Model
import datetime


class ConfigurationView(View):
    def get(self, request):
        headers = ["id", "cameraId", "modelId", "created", "modified"]
        configuration = Configuration.objects.all()
        return render(request, 'dashboard/listConfiguration.html', {'headers': headers, 'data': configuration})

    def put(self, request):
        cameraId = request.PUT['cameraId']
        modelId = request.PUT['modelId']
        created = request.PUT['created']
        modified = request.PUT['modified']
        Configuration.objects.get(id=request.PUT['id']).update(cameraId=cameraId, modelId=modelId, created=created,
                                                               modified=modified)
        return redirect('/dashboard/configurations/')


class ConfigurationCreateView(View):
    def get(self, request):
        cameras = Camera.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/configuration-form.html', {'cameras': cameras, 'models': models})

    def post(self, request):
        cameras = Camera.objects.all()
        models = Model.objects.all()
        camera = cameras.get(id=request.POST['camera'])
        model = models.get(id=request.POST['model'])
        configuration = Configuration(cameraId=camera, modelId=model)
        configuration.save()
        return redirect('/dashboard/configurations/')


class ConfigurationEditView(View):
    def get(self, request, configuration_id):
        configuration = Configuration.objects.get(id=configuration_id)
        return render(request, 'dashboard/configuration-edit.html', {'configuration': configuration})

    def post(self, request, configuration_id):
        cameraId = request.POST['cameraId']
        modelId = request.POST['modelId']
        Configuration.objects.filter(id=configuration_id).update(cameraId=cameraId, modelId=modelId)
        return redirect('/dashboard/configurations/')


class ConfigurationDeleteView(View):
    def get(self, request, configuration_id):
        Configuration.objects.get(id=configuration_id).delete()
        return redirect('/dashboard/configurations/')
