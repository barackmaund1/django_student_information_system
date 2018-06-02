from django.db import models

from sis_users.choices import CLASS_CHOICES, YEAR_GROUP_CHOICES

class ClassGroup(models.Model):
    year_group = models.IntegerField(choices=YEAR_GROUP_CHOICES, null=False)
    class_name = models.CharField(max_length=2, choices=CLASS_CHOICES, null=False)
