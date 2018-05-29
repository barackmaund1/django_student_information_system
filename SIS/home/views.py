from django.views import View
from django.shortcuts import render
from notice_board.models import Announcement
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

class Home(View):
    def get(self, request):
        annoucements = Announcement.objects.order_by('-created')[:5]
        context = {
            'page_title': 'home page',
            'announcements': annoucements
        }
        return render(request, "home.html", context)

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home:home-page'))
