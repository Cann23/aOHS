from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.views import View
from backend.models import Worker, Violation, Camera
from dashboard.views.mixins import GetCountsMixin


class DashboardView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard/dashboard.html', {'counts': GetCountsMixin.get_counts(self)})
