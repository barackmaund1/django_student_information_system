from django.http import HttpResponse
from django.views import View

class BasicHome(View):
    def get(self, request):
        return HttpResponse('This is the homepage.')
