from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import DataError
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

class School(models.Model):
    name = models.CharField(max_length=100)

class Year(models.Model):
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(choices=YEAR_CHOICES, null=False)

    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)
        qs = Year.objects.filter(value=self.value)
        if qs.filter(school=self.school).exists():
            raise ValidationError('Years must be unique within each school.')

    def save(self, *args, **kwargs):
        self.validate_unique()
        super().save(*args, **kwargs)

class Band(models.Model):
    year = models.ForeignKey('Year', on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=1, choices=BAND_CHOICES, null=False)

class Set(models.Model):
    band = models.ForeignKey('Band', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(choices=SET_CHOICES, null=False)
    subjects = models.ManyToManyField('Subject')
    teachers = models.ManyToManyField('sis_users.Staff')

class Subject(models.Model):
    name = models.CharField(max_length=20, null=True)
    teachers = models.ManyToManyField('sis_users.Staff')

    def __str__(self):
        return self.name

class ClassGroup(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES, null=False)
    band = models.CharField(max_length=1, choices=BAND_CHOICES, null=False)
    set = models.IntegerField(choices=SET_CHOICES, null=False)
    subjects = models.ManyToManyField(Subject)
    teachers = models.ManyToManyField('sis_users.Staff')

    def __str__(self):
        year = self.get_year_display()
        band = self.get_band_display()
        set = self.get_set_display()
        return f'{year} - {band} - {set}'

@receiver(pre_save, sender=ClassGroup)
def catch_duplicate_class(sender, instance, **kwargs):
    '''
        Catches duplicate class instances being created by
        checking if the year, band and set are already present.
        If they're not, the instance is saved.
    '''
    try:
        class_group = ClassGroup.objects.get(
            year=instance.year,
            band=instance.band,
            set=instance.set
        )
        # if the above doesn't raise ObjectDoesNotExist, it must be in db
        # therefore a DataError must be raised
        raise DataError('Cannot create duplicate classes.')
    except ObjectDoesNotExist:
        pass
