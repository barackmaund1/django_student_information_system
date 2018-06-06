from django.shortcuts import render
from django.views import View
from django.urls import reverse
from sis_users.mixins import LoginRequiredMessageMixin

class Profile(LoginRequiredMessageMixin, View):
    login_url = '/'
    error_message = 'You need to login using your school email address.'

    def get(self, request):
        return render(request, 'sis_users/profile.html')

