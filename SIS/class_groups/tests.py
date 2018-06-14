from django.test import TestCase
from class_groups.models import (
    School,
    Year,
    Band,
    Set
)
from class_groups.factories import (
    SchoolFactory,
    YearFactory,
    BandFactory,
    SetFactory
)

class SubjectTestCase(TestCase):
    def test_subject_creation(self):
        pass

class SchoolTestCase(TestCase):
    def setUp(self):
        self.school = SchoolFactory()
    def test_school_creation(self):
        school = School.objects.get(pk=self.school.pk)

        self.assertEqual(
            school.name,
            self.school.name
        )

class YearTestCase(TestCase):
    def setUp(self):
        self.year = YearFactory()

    def test_year_creation(self):
        year = Year.objects.get(pk=self.year.pk)

        self.assertEqual(
            year.value,
            self.year.value
        )

        self.assertEqual(
            year.school.name,
            self.year.school.name
        )

class BandTest(TestCase):
    def setUp(self):
        self.band = BandFactory()

    def test_band_creation(self):
        band = Band.objects.get(pk=self.band.pk)

        self.assertEqual(
            band.value,
            self.band.value
        )

        self.assertEqual(
            band.year.value,
            self.band.year.value
        )

        self.assertEqual(
            band.year.school.name,
            self.band.year.school.name
        )

class SetTest(TestCase):
    def setUp(self):
        self.set = SetFactory()

    def test_set_creation(self):
        set = Set.objects.get(pk=self.set.pk)

        self.assertEqual(
            set.value,
            self.set.value
        )

        self.assertEqual(
            set.band.value,
            self.set.band.value
        )

        self.assertEqual(
            set.band.year.value,
            self.set.band.year.value
        )

        self.assertEqual(
            set.band.year.school.name,
            self.set.band.year.school.name
        )