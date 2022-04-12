from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from backend.models import Violation, Camera, Model, Worker, Profile
from dashboard.views.mixins import GetCountsMixin

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user
        profile = Profile.objects.get(user=profile)
        print(profile.profile_picture)
        return render(request, 'dashboard/profile-page.html', {'profile': profile})
