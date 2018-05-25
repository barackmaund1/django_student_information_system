from django.db import models
from django.utils import timezone

# Create your models here.
class Announcement(models.Model):
    created = models.DateTimeField(default=timezone.now)
    header = models.CharField(max_length=50)
    body_text = models.TextField(max_length=500)