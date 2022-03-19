from django.shortcuts import render

# Create your views here.
from django.views import View

from backend.models import Camera, Worker, Violation, Configuration


class IndexView(View):
    def get(self, request):
        return render(request, 'backend/socket.html')

