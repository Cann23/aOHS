from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from backend.models import Violation, Camera, Model, Worker
from dashboard.views.mixins import GetCountsMixin


class ViolationWorkerView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, worker_id):
        headers = ['id', 'cameraId', 'workerId', 'modelId', 'comment', 'created', 'modified']
        data = Violation.objects.filter(valid=True, workerId=worker_id)
        worker = Worker.objects.get(id=worker_id)
        worker_name = worker.name
        worker_title = worker.title
        return render(request, 'dashboard/listWorkerViolation.html',
                      {'headers': headers, 'data': data, 'name': worker_name, 'title': worker_title,
                       'counts': super().get_counts()})


class ViolationDailyView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        headers = ['Camera Name', 'Worker Name', 'Model Name', 'Comment', 'Created', 'Modified']
        data = Violation.objects.filter(valid=True, created__gte=datetime.now() - timedelta(days=1))
        return render(request, 'dashboard/listDailyViolations.html',
                      {'headers': headers, 'data': data, 'counts': super().get_counts()})


class ViolationDailySelectView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, date):
        headers = ['id', 'cameraId', 'workerId', 'modelId', 'comment', 'created']
        data = Violation.objects.filter(valid=True, created__gte=datetime.now() - timedelta(days=date))
        return render(request, 'dashboard/listDailySelectViolation.html',
                      {'headers': headers, 'data': data, 'counts': super().get_counts()})


class ViolationView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        headers = ['Camera Name', 'Worker Name', 'Model Name', 'Comment', 'Created Date',
                   'Modified Date']
        data = Violation.objects.filter(valid=True)

        if 'Camera Name' in request.GET:
            data = Violation.objects.all().order_by('cameraId__name')
        elif 'Worker Name' in request.GET:
            data = Violation.objects.all().order_by('workerId__name')
        elif 'Model Name' in request.GET:
            data = Violation.objects.all().order_by('modelId__name')
        elif 'Comment' in request.GET:
            data = Violation.objects.all().order_by('comment')
        elif 'Created Date' in request.GET:
            data = Violation.objects.all().order_by('created')
        elif 'Modified Date' in request.GET:
            data = Violation.objects.all().order_by('modified')
        return render(request, 'dashboard/listViolation.html',
                      {'headers': headers, 'data': data, 'counts': super().get_counts()})

    def put(self, request):
        cameraId = request.PUT['cameraId']
        workerId = request.PUT['workerId']
        modelId = request.PUT['modelId']
        comment = request.PUT['comment']
        created = request.PUT['created']
        modified = request.PUT['modified']
        Violation.objects.get(id=request.PUT['id']).update(cameraId=cameraId, workerId=workerId, modelId=modelId,
                                                           comment=comment, created=created, modified=modified)
        return redirect('/dashboard/violations/')


class ViolationCaptureView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, violation_id):
        headers = ['id', 'cameraId', 'workerId', 'modelId', 'comment', 'created', 'modified']
        data = Violation.objects.filter(id=violation_id)[0]
        return render(request, 'dashboard/violationCapture.html',
                      {'headers': headers, 'data': data, 'counts': super().get_counts()})


class ViolationCreateView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        cameras = Camera.objects.all()
        workers = Worker.objects.all()
        models = Model.objects.all()
        return render(request, 'dashboard/violation-form.html',
                      {'cameras': cameras, 'workers': workers, 'models': models, 'counts': super().get_counts()})

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


class ViolationEditView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, violation_id):
        cameras = Camera.objects.all()
        workers = Worker.objects.all()
        models = Model.objects.all()
        violation = Violation.objects.get(id=violation_id)
        return render(request, 'dashboard/violation-edit.html',
                      {'violation': violation, 'cameras': cameras, 'workers': workers, 'models': models, 'counts': super().get_counts()})


    def post(self, request, violation_id):
        cameras = Camera.objects.all()
        workers = Worker.objects.all()
        models = Model.objects.all()
        comment = request.POST['comment']
        camera = cameras.get(id=request.POST['camera'])
        worker = workers.get(id=request.POST['worker'])
        model = models.get(id=request.POST['model'])
        print()
        Violation.objects.filter(id=violation_id).update(cameraId=camera, workerId=worker, modelId=model, comment=comment)
        return redirect('/dashboard/violations/')


class ViolationDeleteView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, violation_id):
        Violation.objects.filter(id=violation_id).update(valid=False)
        return redirect('/dashboard/violations')
