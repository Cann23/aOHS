from django.views.decorators import gzip
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import StreamingHttpResponse, HttpResponseServerError, HttpResponse
from django.shortcuts import render, redirect

from django.views import View
import os
from backend.models import Camera, Profile
from dashboard.views.mixins import GetCountsMixin
import cv2


class CameraCreateView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        specialists = Profile.objects.filter(role='SP')
        return render(request, 'dashboard/camera-form.html', {'specialists': specialists, 'counts': super().get_counts()})

    def post(self, request):
        print(request.POST['specialist'])
        user = Profile.objects.filter(id=request.POST['specialist']).first().user
        cameras = Camera(name=request.POST['camera_name'], url=request.POST['camera_url'], userId=user)
        cameras.save()
        return redirect('/dashboard/cameras/')


class CameraView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        headers = ['name', 'url', 'active']
        cameras = Camera.objects.all()
        if 'name' in request.GET:
            cameras = Camera.objects.all().order_by('name')
        elif 'url' in request.GET:
            cameras = Camera.objects.all().order_by('url')
        return render(request, 'dashboard/listCamera.html',
                      {'headers': headers, 'data': cameras, 'counts': super().get_counts()})


class CameraEditView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, camera_id):
        camera = Camera.objects.get(id=camera_id)
        specialists = Profile.objects.filter(role='SP')
        return render(request, 'dashboard/camera-edit.html', {'specialists': specialists, "camera": camera, 'counts': super().get_counts()})

    def post(self, request, camera_id):
        name = request.POST['name']
        url = request.POST['url']
        active = request.POST['active']
        Camera.objects.filter(id=camera_id).update(name=name, url=url, active=active)
        return redirect('/dashboard/cameras')


class CameraDeleteView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, camera_id):
        Camera.objects.get(id=camera_id).delete()
        return redirect('/dashboard/cameras/', {'counts': super().get_counts()})


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def index(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")


class ImageView(View):
    def get(self, request, id):
        # if id != 0:
        #     os.remove(f"/home/enssr/Desktop/ceng4-1/ceng491/seace/lib/Helmet-Vest-Worker/frames/{id-1}.jpg")
        # with open(f"/home/enssr/Desktop/ceng4-1/ceng491/seace/lib/Helmet-Vest-Worker/frames/{id}.jpg", "rb") as f:
        #     return HttpResponse(f.read(), content_type="image/jpeg")
        with open(f"/home/enssr/Desktop/ceng4-1/ceng491/seace/src/capture0.jpg", "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpg")


class Home(View):
    def get(self, request):
        return render(request, 'dashboard/home.html')
