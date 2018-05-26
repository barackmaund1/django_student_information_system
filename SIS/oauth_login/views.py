from django.views import View
from django.http import HttpResponse

class LoginView(View):
    def get(self, request):
        return HttpResponse("You're at the login page.")
