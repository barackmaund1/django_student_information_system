from django.urls import path
from sis_users.views import (
    AdminList,
    AdminDetail,
    StaffList,
    StaffDetail,
    StudentList,
    StudentDetail,
    Profile
)

app_name = 'sis_users'

urlpatterns = [
    path('profile', Profile.as_view(), name='profile'),
    path('admins', AdminList.as_view(), name='admin-list'),
    path('admins/<username>', AdminDetail.as_view(), name='admin-detail'),
    path('staff', StaffList.as_view(), name='staff-list'),
    path('staff/<username>', StaffDetail.as_view(), name='staff-detail'),
    path('students', StudentList.as_view(), name='student-list'),
    path('students/<username>', StudentDetail.as_view(), name='student-detail'),
]