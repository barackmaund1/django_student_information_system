from django.views.generic import ListView, DetailView
from sis_users.mixins import LoginRequiredMessageMixin
from sis_users.models import Admin, Staff, Student


class AdminList(LoginRequiredMessageMixin, ListView):
    template_name = 'sis_users/admin_list.html'

    def get_queryset(self):
        return Admin.objects.all()

class StaffList(LoginRequiredMessageMixin, ListView):
    template_name = 'sis_users/staff_list.html'

    def get_queryset(self):
        return Staff.objects.all()

class StudentList(LoginRequiredMessageMixin, ListView):
    template_name = 'sis_users/student_list.html'

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
