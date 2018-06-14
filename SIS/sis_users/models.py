from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    set = models.ForeignKey('class_groups.Set',
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True)

    def __str__(self):
        return f'{self.user.email}'

class UserState(models.Model):
    '''
        Model to hold whether an email address is a staff member or a student.
        Table will be populated by an external script (run once every hour),
        that will use Google App Manager (GAM) to check email groups and
        determine if a user is a staff member or a student.
    '''
    email = models.EmailField(default='', unique=True)
    staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    year = models.IntegerField(choices=YEAR_CHOICES, null=True)
    band = models.CharField(max_length=1, choices=BAND_CHOICES, null=True)
    set = models.IntegerField(choices=SET_CHOICES, null=True)

    def __str__(self):
        return f'{self.email} - Admin: {self.is_admin} - Staff: {self.staff}'

@receiver(post_save, sender=User)
def create_student_or_staff(sender, instance, created, **kwargs):
    if created:
        state = UserState.objects.get(
            email=instance.email
        )
        if state.staff:
            if state.is_admin:
                Admin.objects.create(
                    user=instance
                )
            Staff.objects.create(
                user=instance
            )
        else:
            class_instance = None
            if state.year and state.band and state.set:
                class_model = apps.get_model('class_groups.Set')
                class_instance = class_model.objects.get(
                    value=state.set,
                    band__value=state.band,
                    band__year__value=state.year
                )
            Student.objects.create(
                user=instance,
                set=class_instance
            )
            

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    if hasattr(instance, 'admin'):
        instance.admin.save()
    if hasattr(instance, 'staff'):
        instance.staff.save()
    if hasattr(instance, 'student'):
        instance.student.save()
