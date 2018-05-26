from django.urls import path
from oauth_login.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login-view')
]