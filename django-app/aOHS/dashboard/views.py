from django.shortcuts import render, redirect

from django.views import View

from backend.models import Worker, Violation, Model, Configuration, Camera


class Obj:
    def __init__(self):
        self.x = 'x'
        self.y = 'y'
        self.z = 'z'


class Example(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


class Example2(View):
    def get(self, request):
        headers = ['a', 'b', 'c']
        data = [Obj(), Obj(), Obj()]
        return render(request, 'dashboard/list.html', {'headers': headers, 'data': data})


class WorkerCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/worker-form.html')

    def post(self, request):
        worker = Worker(name=request.POST['worker_name'], title=request.POST['worker_title'],
                        phone=request.POST['worker_tel'])
        worker.save()
        return redirect('/dashboard/workers/')


class CameraCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/camera-form.html')

    def post(self, request):
        cameras = Camera(name=request.POST['camera_name'], url=request.POST['camera_url'])
        cameras.save()
        return redirect('/dashboard/cameras/')


class ConfigurationCreateView(View):
    def get(self, request):
        cameras = Camera.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/configuration-form.html', {'cameras': cameras, 'models': models})

    def post(self, request):
        cameras = Camera.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/configuration-form.html')


class ViolationView(View):
    def get(self, request):
        headers = ['id', 'cameraId', 'workerId', 'modelId', 'comment', 'created', 'modified']
        data = Violation.objects.all()
        return render(request, 'dashboard/listViolation.html', {'headers': headers, 'data': data})

    def post(self, request):
        violation = Violation(cameraId=request.POST['cameraId'], workerId=request.POST['workerId'],
                              modelId=request.POST['modelId'], comment=request.POST['comment'],
                              created=request.POST['created'], modified=request.POST['modified'])
        violation.save()
        return redirect('dashboard/violations/')

    def put(self, request):
        cameraId = request.PUT['cameraId']
        workerId = request.PUT['workerId']
        modelId = request.PUT['modelId']
        comment = request.PUT['comment']
        created = request.PUT['created']
        modified = request.PUT['modified']
        Violation.objects.get(id=request.PUT['id']).update(cameraId=cameraId, workerId=workerId, modelId=modelId,
                                                           comment=comment, created=created, modified=modified)
        return redirect('dashboard/violations/')

    def delete(self, request):
        Violation.objects.get(id=request.DELETE['id']).delete()
        return redirect('dashboard/violations/')


class WorkerView(View):
    def get(self, request):
        headers = ['id', 'name', 'title', 'phone']
        workers = Worker.objects.all()
        return render(request, 'dashboard/listWorker.html', {'headers': headers, 'data': workers})

    def post(self, request):
        worker = Worker(name=request.POST['name'], title=request.POST['title'], phone=request.POST['phone'])
        worker.save()
        return redirect('dashboard/workers')

    def put(self, request):
        name = request.PUT['name']
        title = request.PUT['title']
        phone = request.PUT['phone']
        Worker.objects.get(id=request.PUT['id']).update(name=name, title=title, phone=phone)
        return redirect('dashboard/workers')

    def delete(self, request):
        Worker.objects.get(id=request.DELETE['id']).delete()
        return redirect('dashboard/workers')


class ModelView(View):
    def get(self, request):
        headers = ['id', 'name', 'path']
        models = Model.objects.all()
        return render(request, 'dashboard/listModel.html', {'headers': headers, 'data': models})

    def post(self, request):
        worker = Model(name=request.POST['name'], path=request.POST['path'])
        worker.save()
        return redirect('dashboard/models')

    def put(self, request):
        name = request.PUT['name']
        path = request.PUT['path']
        Model.objects.get(id=request.PUT['id']).update(name=name, path=path)
        return redirect('dashboard/models')

    def delete(self, request):
        Model.objects.get(id=request.DELETE['id']).delete()
        return redirect('dashboard/models')


class ConfigurationView(View):
    def get(self, request):
        headers = ["id", "cameraId", "modelId", "created", "modified"]
        configuration = Configuration.objects.all()
        return render(request, 'dashboard/listConfiguration.html', {'headers': headers, 'data': configuration})

    def post(self, request):
        configuration = Configuration(cameraId=request.POST['cameraId'], modelId=request.POST['modelId'],
                                      created=request.POST['created'], modified=request.POST['modified'])
        configuration.save()
        return redirect('dasboard/configurations/')

    def put(self, request):
        cameraId = request.PUT['cameraId']
        modelId = request.PUT['modelId']
        created = request.PUT['created']
        modified = request.PUT['modified']
        Configuration.objects.get(id=request.PUT['id']).update(cameraId=cameraId, modelId=modelId, created=created,
                                                               modified=modified)
        return redirect('dasboard/configurations/')

    def delete(self, request):
        Configuration.objects.get(id=request.DELETE['id']).delete()
        return redirect('dasboard/configurations/')


class CameraView(View):
    def get(self, request):
        headers = ['name', 'url']
        cameras = Camera.objects.all()
        return render(request, 'dashboard/listCamera.html', {'headers': headers, 'data': cameras})
