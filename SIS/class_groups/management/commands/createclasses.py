from django.core.management import BaseCommand
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES
from class_groups.models import ClassGroup

YEAR_CHOICES = [c[0] for c in YEAR_CHOICES]
BAND_CHOICES = [c[0] for c in BAND_CHOICES]
SET_CHOICES = [c[0] for c in SET_CHOICES]

class Command(BaseCommand):
    def handle(self, *args, **options):
        classes = []
        for YEAR in YEAR_CHOICES:
            for BAND in BAND_CHOICES:
                for SET in SET_CHOICES:
                    classes.append(ClassGroup(
                        year=YEAR,
                        band=BAND,
                        set=SET
                    ))
        for c in classes:
            c.save()

        self.stdout.write('Successfully created the following classes:')
        for c in classes:
            self.stdout.write(c.__str__())
