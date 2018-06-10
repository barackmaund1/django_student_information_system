from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import DataError
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Year(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(choices=YEAR_CHOICES, null=False)

    def __str__(self):
        return self.get_value_display()

    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)
        qs = Year.objects.filter(value=self.value)
        if qs.filter(school=self.school).exists():
            raise ValidationError('Years must be unique within each school.')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.validate_unique()
        super().save(*args, **kwargs)

class Band(models.Model):
    year = models.ForeignKey('Year', on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=1, choices=BAND_CHOICES, null=False)

    def __str__(self):
        year = self.year.get_value_display()
        band = self.get_value_display()
        return f'{year} - {band}'

    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)
        qs = Band.objects.filter(value=self.value)
        if qs.filter(year=self.year).exists():
            if qs.filter(year__school=self.year.school).exists():
                raise ValidationError('Each band must be unique within each year group.')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.validate_unique()
        super().save(*args, **kwargs)

class Set(models.Model):
    band = models.ForeignKey('Band', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(choices=SET_CHOICES, null=False)
    subjects = models.ManyToManyField('Subject')
    teachers = models.ManyToManyField('sis_users.Staff')

    def __str__(self):
        year = self.band.year.get_value_display()
        band = self.band.get_value_display()
        set = self.get_value_display()
        return f'{year} - {band} - {set}'

    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)
        qs = Set.objects.filter(value=self.value)
        if qs.filter(band=self.band).exists():
            if qs.filter(band__year=self.band.year).exists():
                if qs.filter(band__year__school=self.band.year.school).exists():
                    raise ValidationError('Each set must be unique within each band.')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.validate_unique()
        super().save(*args, **kwargs)

class Subject(models.Model):
    name = models.CharField(max_length=20, null=True)
    teachers = models.ManyToManyField('sis_users.Staff')

    def __str__(self):
        return self.name
