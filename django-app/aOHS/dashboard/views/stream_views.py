from django.views import View

from backend.models import Camera
from django.shortcuts import render, redirect

class StreamView(View):
    def get(self, request):
        cameras = Camera.objects.all()
        return render(request, 'dashboard/stream-form.html', {'cameras': cameras})
