from django.shortcuts import render
from django.views import View
from django.urls import reverse
from sis_users.mixins import LoginRequiredMessageMixin

class Profile(LoginRequiredMessageMixin, View):
    def get(self, request):
        return render(request, 'sis_users/profile.html')

