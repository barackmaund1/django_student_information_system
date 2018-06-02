from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sis_users.choices import CLASS_CHOICES, YEAR_GROUP_CHOICES

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_group = models.CharField(max_length=4, choices=CLASS_CHOICES, null=True)
    year_group = models.IntegerField(choices=YEAR_GROUP_CHOICES, null=True)

    def get_full_class_name(self):
        class_group = self.get_class_group_display()
        year_group = self.get_year_group_display()
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
    class_group = models.CharField(max_length=4, choices=CLASS_CHOICES, null=True)
    year_group = models.IntegerField(choices=YEAR_GROUP_CHOICES, null=True)

@receiver(post_save, sender=User)
def create_student_or_staff(sender, instance, created, **kwargs):
    ''' Create a User instance based on whether they are staff or student '''
    if created:
        state = UserState.objects.get(
            email_address=instance.email
        )
        if state.staff:
            Staff.objects.create(
                user=instance
            )
        else:
            Student.objects.create(
                user=instance,
                class_group=state.class_group,
                year_group=state.year_group
            )

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    if hasattr(instance, 'staff'):
        instance.staff.save()
    if hasattr(instance, 'student'):
        instance.student.save()
