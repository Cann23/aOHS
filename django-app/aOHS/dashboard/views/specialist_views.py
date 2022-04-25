from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from backend.models import Worker, Profile, Camera
from dashboard.views.mixins import GetCountsMixin


class SpecialistView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        headers = ['id', 'specialist_name']
        workers = Worker.objects.filter(active=True)

        specialists = Profile.objects.filter(role='SP')
        return render(request, 'dashboard/list-specialist.html',
                      {'headers': headers, 'data': specialists, 'counts': super().get_counts()})


class SpecialistCreateView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard/specialist-form.html', {'counts': super().get_counts()})

    def post(self, request):
        worker = Worker(name=request.POST['worker_name'], title=request.POST['worker_title'],
                        phone=request.POST['worker_tel'])
        worker.save()
        return redirect('/dashboard/Specialists/')


class SpecialistEditView(LoginRequiredMixin, View, GetCountsMixin):
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


class SpecialistDeleteView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, specialist_id):
        print(specialist_id)

        User.objects.filter(id=Profile.objects.get(id=specialist_id).user_id).delete()
        return redirect('/dashboard/specialists/', {'counts': super().get_counts()})


class SpecialistCameraView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, specialist_id):
        headers = ['name', 'url']
        user = Profile.objects.get(id=specialist_id).user
        print(user)
        cameras = Camera.objects.filter(userId=user)
        return render(request, 'dashboard/listCamera.html',
                      {'headers': headers, 'data': cameras, 'counts': super().get_counts()})

