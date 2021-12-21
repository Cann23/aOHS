from django.shortcuts import render

# Create your views here.
from django.views import View


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

