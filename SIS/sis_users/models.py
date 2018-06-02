from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_group = models.ForeignKey('class_groups.ClassGroup', on_delete=models.SET_NULL, null=True)

class UserState(models.Model):
    '''
        Model to hold whether an email address is a staff member or a student.
        Table will be populated by an external script (run once every hour),
        that will use Google App Manager (GAM) to check email groups and
        determine if a user is a staff member or a student.
    '''
    email_address = models.EmailField(default='')
    staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    year = models.IntegerField(choices=YEAR_CHOICES, null=True)
    band = models.CharField(max_length=1, choices=BAND_CHOICES, null=True)
    set = models.IntegerField(choices=SET_CHOICES, null=True)

@receiver(post_save, sender=User)
def create_student_or_staff(sender, instance, created, **kwargs):
    ''' Create a User instance based on whether they are staff or student '''
    if created:
        state = UserState.objects.get(
            email_address=instance.email
        )
        if state.staff:
            Staff.objects.create(
                user=instance,
                is_admin=state.is_admin
            )
        else:
            class_instance = None
            if state.year and state.band and state.set:
                class_model = apps.get_model('class_groups.ClassGroup')
                class_instance = class_model.objects.get(
                    year=state.year,
                    band=state.band,
                    set=state.set
                )
            Student.objects.create(
                user=instance,
                class_group=class_instance
            )

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    if hasattr(instance, 'staff'):
        instance.staff.save()
    if hasattr(instance, 'student'):
        instance.student.save()
