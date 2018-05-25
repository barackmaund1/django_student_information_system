from django.urls import path
from home.views import BasicHome

urlpatterns = [
    path('', BasicHome.as_view(), name='home-page')
]