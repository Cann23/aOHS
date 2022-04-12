from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from backend.models import Profile


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user
        profile = Profile.objects.get(user=profile)
        print(profile.profile_picture)
        return render(request, 'dashboard/profile-page.html', {'profile': profile})

    def post(self, request):
        # profile = request.user
        # profile = Profile.objects.get(user=profile)
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        # profile.phone_number = request.POST['phone_number']
        request.user.save()
        return redirect('/dashboard/')


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user
        profile = Profile.objects.get(user=profile)
        return render(request, 'dashboard/profile-edit.html', {'profile': profile})

    def post(self, request):
        profile = request.user
        profile = Profile.objects.get(user=profile)
        profile.user.first_name = request.POST['first_name']
        profile.user.last_name = request.POST['last_name']
        profile.user.email = request.POST['email']
        # profile.phone_number = request.POST['phone_number']
        profile.save()
        return redirect('profile')
