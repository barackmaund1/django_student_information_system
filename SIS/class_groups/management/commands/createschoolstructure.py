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

