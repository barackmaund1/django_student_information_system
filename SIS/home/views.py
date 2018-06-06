from django.views import View
from django.shortcuts import render
from notice_board.models import Announcement
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from sis_users.models import Staff, Student

class Home(View):
    def get(self, request):
        annoucements = Announcement.objects.order_by('-created')[:5]
        user = request.user

        context = {
            'page_title': 'home page',
            'announcements': annoucements,
        }
        if not request.user.is_anonymous:
            if hasattr(user, 'staff'):
                user_state = 'staff'
            elif hasattr(user, 'student'):
                user_state = 'student'
            elif hasattr(user, 'admin'):
                user_state = 'admin'
            else:
                if user.is_superuser:
                    user_state = 'super user'
                else:
                    user_state = ''
            context['user_state'] = user_state

        return render(request, "home/home.html", context)

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home:home-page'))
