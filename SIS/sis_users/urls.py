from django.urls import path
from sis_users.views import Profile

app_name = 'sis_users'

urlpatterns = [
    path('profile/', Profile.as_view(), name='profile')
]