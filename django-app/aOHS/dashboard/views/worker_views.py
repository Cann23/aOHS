from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from backend.models import Worker
from dashboard.views.mixins import GetCountsMixin


class WorkerView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        headers = ['id', 'name', 'title', 'phone']
        workers = Worker.objects.filter(active=True)
        return render(request, 'dashboard/listWorker.html',
                      {'headers': headers, 'data': workers, 'counts': super().get_counts()})


class WorkerCreateView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard/worker-form.html', {'counts': super().get_counts()})

    def post(self, request):
        worker = Worker(name=request.POST['worker_name'], title=request.POST['worker_title'],
                        phone=request.POST['worker_tel'])
        worker.save()
        return redirect('/dashboard/workers/')


class WorkerEditView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, worker_id):
        worker = Worker.objects.get(id=worker_id)
        return render(request, 'dashboard/worker-edit.html', {"worker": worker, 'counts': super().get_counts()})

    def post(self, request, worker_id):
        name = request.POST['name']
        title = request.POST['title']
        phone = request.POST['phone']
        Worker.objects.filter(id=worker_id).update(name=name, title=title, phone=phone)
        return redirect('/dashboard/workers')


class WorkerDeleteView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, worker_id):
        Worker.objects.filter(id=worker_id).update(active=False)
        return redirect('/dashboard/workers')
