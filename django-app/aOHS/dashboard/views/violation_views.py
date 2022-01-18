from django.shortcuts import render, redirect

from django.views import View

from backend.models import Violation, Camera, Model, Worker


class ViolationView(View):
    def get(self, request):
        headers = ['id', 'cameraId', 'workerId', 'modelId', 'comment', 'created', 'modified']
        data = Violation.objects.all()
        return render(request, 'dashboard/listViolation.html', {'headers': headers, 'data': data})

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

class ViolationCreateView(View):
    def get(self, request):
        cameras = Camera.objects.all()
        workers = Worker.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/violation-form.html', {'cameras': cameras, 'workers': workers, 'models': models})

    def post(self, request):
        cameras = Camera.objects.all()
        workers = Worker.objects.all()
        models = Model.objects.all()
        comment = request.POST['comment']
        camera = cameras.get(id=request.POST['camera'])
        worker = workers.get(id=request.POST['worker'])
        model = models.get(id=request.POST['model'])
        violation = Violation(cameraId=camera, workerId=worker, modelId=model, comment=comment)
        violation.save()
        return redirect('/dashboard/violations/')

class ViolationEditView(View):
    def get(self, request, violation_id):
        violation = Violation.objects.get(id=violation_id)
        return render(request, 'dashboard/violation-edit.html', {'violation': violation})

    def post(self, request, violation_id):
        cameraId = request.POST['cameraId']
        workerId = request.POST['workerId']
        modelId = request.POST['modelId']
        comment = request.POST['comment']
        Violation.objects.filter(id=violation_id).update(cameraId=cameraId, workerId=workerId, modelId=modelId, comment=comment)
        return redirect('/dashboard/violations/')

class ViolationDeleteView(View):
    def get(self, request, violation_id):
        Violation.objects.filter(id=violation_id).update(valid=False)
        return redirect('/dashboard/violations')