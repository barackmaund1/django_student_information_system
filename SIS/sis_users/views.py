from django.views.generic import ListView, DetailView
from sis_users.mixins import (
    LoginRequiredMessageMixin,
    BaseAccessMessageMixin
)
from sis_users.models import Admin, Staff, Student

class AdminList(BaseAccessMessageMixin, ListView):
    template_name = 'sis_users/admin_list.html'
    permitted_attributes = ['admin']
    error_message = 'You must be an administrator to access this page.'

    def get_queryset(self):
        return Admin.objects.all()

class StaffList(BaseAccessMessageMixin, ListView):
    template_name = 'sis_users/staff_list.html'
    permitted_attributes = ['admin', 'staff']
    error_message = 'You must be a staff member, or administrator to access this page.'

    def get_queryset(self):
        return Staff.objects.all()

class StudentList(BaseAccessMessageMixin, ListView):
    template_name = 'sis_users/student_list.html'
    permitted_attributes = ['admin', 'staff', 'student']
    error_message = 'You must be a staff member, administrator or student to access this page.'

    def get_queryset(self):
        return Student.objects.all()

class AdminDetail(LoginRequiredMessageMixin, DetailView):
    template_name = 'sis_users/admin_profile.html'

    def get_object(self, queryset=None):
        return Admin.objects.get(user__username=self.kwargs['username'])


class StaffDetail(LoginRequiredMessageMixin, DetailView):
    template_name = 'sis_users/staff_profile.html'

    def get_object(self, queryset=None):
        return Staff.objects.get(user__username=self.kwargs['username'])

class StudentDetail(LoginRequiredMessageMixin, DetailView):
    template_name = 'sis_users/student_profile.html'

    def get_object(self, queryset=None):
        return Student.objects.get(user__username=self.kwargs['username'])
