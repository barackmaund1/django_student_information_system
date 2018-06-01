from django.db import models
from django.contrib.auth.models import User
from sis_users.choices import CLASS_CHOICES, YEAR_GROUP_CHOICES

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_group = models.CharField(max_length=4, choices=CLASS_CHOICES, null=True)
    year_group = models.IntegerField(choices=YEAR_GROUP_CHOICES, null=True)

    def get_full_class_name(self, user_id):
        user = User.objects.get(pk=user_id)
        year_group = user.year_group
        class_group = user.class_group
        return f'{year_group} - {class_group}'

class UserState(models.Model):
    '''
        Model to hold whether an email address is a staff member or a student.
        Table will be populated by an external script (run once every hour),
        that will use Google App Manager (GAM) to check email groups and
        determine if a user is a staff member or a student.
    '''
    email_address = models.EmailField(default='')
    staff = models.BooleanField(default=False)


