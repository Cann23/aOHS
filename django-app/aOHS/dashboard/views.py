from django.shortcuts import render, redirect

from django.views import View

from backend.models import Worker


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


class WorkerView(View):
    def get(self, request):
        headers = ['id', 'name', 'title', 'phone']
        workers = Worker.objects.all()
        return render(request, 'dashboard/worker_list.html', {'headers': headers, 'data': workers})

    def post(self, request):
        worker = Worker(name=request.POST['name'], title=request.POST['title'], phone=request.POST['phone'])
        worker.save()
        return redirect('dashboard/worker_list.html')

    def put(self, request):
        name = request.PUT['name']
        title = request.PUT['title']
        phone = request.PUT['phone']
        Worker.objects.get(id=request.PUT['id']).update(name=name, title=title, phone=phone)
        return redirect('dashboard/worker_list.html')

    def delete(self, request):
        Worker.objects.get(id=request.DELETE['id']).delete()
        return redirect('dashboard/worker_list.html')
