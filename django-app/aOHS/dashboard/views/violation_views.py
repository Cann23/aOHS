from django.shortcuts import render, redirect

from django.views import View

from backend.models import Violation


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
