from django.contrib import admin
from sis_users.models import Admin, Staff, Student

class AdminAdmin(admin.ModelAdmin):
    pass

class StaffAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Admin, AdminAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Student, StudentAdmin)
