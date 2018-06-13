from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.contrib import messages

class BaseAccessMessageMixin(AccessMixin):
    permitted_attributes = []
    error_message = ''

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        permitted = self.get_permitted_attributes()
        if user.is_authenticated:
            if True in [hasattr(user, attr) for attr in permitted] or '__all__' in permitted:
                return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()

    def get_error_message(self):
        return self.error_message

    def get_permitted_attributes(self):
        return self.permitted_attributes

    def handle_no_permission(self):
        messages.error(self.request, self.get_error_message())
        return super().handle_no_permission()

class LoginRequiredMessageMixin(LoginRequiredMixin):
    login_url = '/'
    error_message = 'You need to login using your school email address.'

    def get_error_message(self):
        return self.error_message

    def handle_no_permission(self):
        messages.error(self.request, self.get_error_message())
        return super(LoginRequiredMessageMixin, self).handle_no_permission()
