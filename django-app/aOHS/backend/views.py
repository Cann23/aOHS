from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from backend.models import Camera, Worker, Violation, Configuration


class IndexView(View):
    def get(self, request):
        return redirect('/dashboard/')

