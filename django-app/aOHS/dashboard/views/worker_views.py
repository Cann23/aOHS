from django.shortcuts import render, redirect

from django.views import View

from backend.models import Worker


class WorkerView(View):
    def get(self, request):
        headers = ['id', 'name', 'title', 'phone']
        workers = Worker.objects.all()
        return render(request, 'dashboard/listWorker.html', {'headers': headers, 'data': workers})

    def delete(self, request):
        Worker.objects.get(id=request.DELETE['id']).delete()
        return redirect('dashboard/workers')


class WorkerCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/worker-form.html')

    def post(self, request):
        worker = Worker(name=request.POST['worker_name'], title=request.POST['worker_title'],
                        phone=request.POST['worker_tel'])
        worker.save()
        return redirect('/dashboard/workers/')


class WorkerEditView(View):
    def get(self, request, worker_id):
        worker = Worker.objects.get(id=worker_id)
        return render(request, 'dashboard/worker-edit.html', {"worker": worker})

    def post(self, request, worker_id):
        name = request.POST['name']
        title = request.POST['title']
        phone = request.POST['phone']
        Worker.objects.filter(id=worker_id).update(name=name, title=title, phone=phone)
        return redirect('/dashboard/workers')
