from django.db import models

from sis_users.choices import CLASS_CHOICES, YEAR_GROUP_CHOICES

class Subject(models.Model):
    subject_name = models.CharField(max_length=20, null=True)

class ClassGroup(models.Model):
    year_group = models.IntegerField(choices=YEAR_GROUP_CHOICES, null=False)
    class_name = models.CharField(max_length=2, choices=CLASS_CHOICES, null=False)
    subjects = models.ManyToManyField(Subject)
