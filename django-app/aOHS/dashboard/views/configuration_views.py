from django.shortcuts import render, redirect

from django.views import View

from backend.models import Configuration, Camera, Model


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
        return redirect('dashboard/configurations/')

    def delete(self, request):
        Configuration.objects.get(id=request.DELETE['id']).delete()
        return redirect('dasboard/configurations/')


class ConfigurationCreateView(View):
    def get(self, request):
        cameras = Camera.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/configuration-form.html', {'cameras': cameras, 'models': models})

    def post(self, request):
        cameras = Camera.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/configuration-form.html')
