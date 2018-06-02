from django.db import models

from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

class Subject(models.Model):
    name = models.CharField(max_length=20, null=True)
    teachers = models.ManyToManyField('sis_users.Staff')

class ClassGroup(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES, null=False)
    band = models.CharField(max_length=1, choices=BAND_CHOICES, null=False)
    set = models.IntegerField(choices=SET_CHOICES, null=False)
    subjects = models.ManyToManyField(Subject)
    teachers = models.ManyToManyField('sis_users.Staff')
