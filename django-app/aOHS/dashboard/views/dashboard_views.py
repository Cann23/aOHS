from django.shortcuts import render, redirect

from django.views import View
from backend.models import Worker, Violation, Camera


class DashboardView(View):
    def get(self, request):
        counts = {
            'workers': Worker.objects.count(),
            'violations': Violation.objects.count(),
            'cameras': Camera.objects.count(),
        }
        return render(request, 'dashboard/dashboard.html', {'counts': counts})
