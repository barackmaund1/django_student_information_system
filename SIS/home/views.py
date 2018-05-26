from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from notice_board.models import Announcement

class BasicHome(View):
    def get(self, request):
        annoucements = Announcement.objects.order_by('-created')[:5]
        context = {
            'page_title': 'home page',
            'announcements': annoucements
        }
        return render(request, "home.html", context)
