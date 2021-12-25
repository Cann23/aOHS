from django.shortcuts import render, redirect

from django.views import View

from backend.models import Camera


class CameraCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/camera-form.html')

    def post(self, request):
        cameras = Camera(name=request.POST['camera_name'], url=request.POST['camera_url'])
        cameras.save()
        return redirect('/dashboard/cameras/')


class CameraView(View):
    def get(self, request):
        headers = ['name', 'url']
        cameras = Camera.objects.all()
        return render(request, 'dashboard/listCamera.html', {'headers': headers, 'data': cameras})
