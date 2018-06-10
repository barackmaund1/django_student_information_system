import faker
from factory.django import DjangoModelFactory
from factory import lazy_attribute
from random import choice
from class_groups.models import ClassGroup, Subject, School, Year, Band, Set
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

faker = faker.Factory.create()

class SchoolFactory(DjangoModelFactory):
    class Meta:
        model = School

    name = lazy_attribute(lambda x: faker.sentence(nb_words=4))

class YearFactory(DjangoModelFactory):
    class Meta:
        model = Year

    school = lazy_attribute(lambda x: SchoolFactory())
    value = lazy_attribute(lambda x: choice([c[0] for c in YEAR_CHOICES]))

class BandFactory(DjangoModelFactory):
    class Meta:
        model = Band

    year = lazy_attribute(lambda x: YearFactory())
    value = lazy_attribute(lambda x: choice([c[0] for c in BAND_CHOICES]))

class SetFactory(DjangoModelFactory):
    class Meta:
        model = Set

    band = lazy_attribute(lambda x: BandFactory())
    value = lazy_attribute(lambda x: choice([c[0] for c in SET_CHOICES]))

class ClassGroupFactory(DjangoModelFactory):
    class Meta:
        model = ClassGroup

    year = lazy_attribute(lambda x: choice([c[0] for c in YEAR_CHOICES]))
    band = lazy_attribute(lambda x: choice([c[0] for c in BAND_CHOICES]))
    set = lazy_attribute(lambda x: choice([c[0] for c in SET_CHOICES]))

class SubjectFactory(DjangoModelFactory):
    class Meta:
        model = Subject

    name = lazy_attribute(lambda x: faker.word())