from django.core.management import BaseCommand
from django.conf import settings
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES
from class_groups.models import School, Year, Band, Set

YEAR_CHOICES = [c[0] for c in YEAR_CHOICES]
BAND_CHOICES = [c[0] for c in BAND_CHOICES]
SET_CHOICES = [c[0] for c in SET_CHOICES]

class Command(BaseCommand):
    '''
        Creates the basic school organisational structure
        - School
        - Years
        - Bands
        - Sets
        Each are nested inside each other.
    '''
    def handle(self, *args, **options):
        school_name = settings.SCHOOL_NAME
        school = School.objects.create(name=school_name)
        years = [Year(value=v) for v in YEAR_CHOICES]
        [year.save() for year in years]
        for year in years:
            school.year_set.add(year)
            school.save()
            bands = [Band(value=v) for v in BAND_CHOICES]
            [band.save() for band in bands]
            for band in bands:
                year.band_set.add(band)
                year.save()
                sets = [Set(value=v) for v in SET_CHOICES]
                [set.save() for set in sets]
                for set in sets:
                    band.set_set.add(set)
                    band.save()
        created_sets = Set.objects.all()
        self.stdout.write(f'Created the following {created_sets.count()} classes:')
        for set in created_sets:
            self.stdout.write(set.__str__())

