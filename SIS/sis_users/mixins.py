from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class LoginRequiredMessageMixin(LoginRequiredMixin):
    login_url = '/'
    error_message = 'You need to login using your school email address.'

    def get_error_message(self):
        return self.error_message

    def handle_no_permission(self):
        messages.error(self.request, self.get_error_message())
        return super(LoginRequiredMessageMixin, self).handle_no_permission()
