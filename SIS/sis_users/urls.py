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
    path('admin', AdminList.as_view(), name='admin-list'),
    path('admin/<username>', AdminDetail.as_view(), name='admin-detail'),
    path('staff', StaffList.as_view(), name='staff-list'),
    path('staff/<username>', StaffDetail.as_view(), name='staff-detail'),
    path('student', StudentList.as_view(), name='student-list'),
    path('student/<username>', StudentDetail.as_view(), name='student-detail'),
]