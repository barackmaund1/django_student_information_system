from django.urls import path
from home.views import Home, Logout

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('logout', Logout.as_view(), name='logout')
]