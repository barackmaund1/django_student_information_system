from factory import DjangoModelFactory, lazy_attribute, SubFactory
from django.contrib.auth.models import User
import faker
from random import choice

from sis_users.models import Admin, Staff, Student, UserState
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

faker = faker.Factory.create()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = lazy_attribute(lambda x: faker.user_name())
    first_name = lazy_attribute(lambda x: faker.first_name())
    last_name = lazy_attribute(lambda x: faker.last_name())
    email = lazy_attribute(lambda x: faker.email())
    password = lazy_attribute(lambda x: faker.password())

class AdminStateFactory(DjangoModelFactory):
    class Meta:
        model = UserState

    email = lazy_attribute(lambda x: faker.email())
    staff = True
    is_admin = True

class StaffStateFactory(DjangoModelFactory):
    class Meta:
        model = UserState

    email = lazy_attribute(lambda x: faker.email())
    staff = True
    is_admin = False

class StudentStateFactory(DjangoModelFactory):
    class Meta:
        model = UserState

    email = lazy_attribute(lambda x: faker.email())
    staff = False
    is_admin = False
    year = lazy_attribute(lambda x: choice(YEAR_CHOICES))
    band = lazy_attribute(lambda x: choice(BAND_CHOICES))
    set = lazy_attribute(lambda x: choice(SET_CHOICES))

class AdminFactory(DjangoModelFactory):
    class Meta:
        model = Admin
        django_get_or_create = ('user',)

    user = SubFactory(UserFactory)

class StaffFactory(DjangoModelFactory):
    class Meta:
        model = Staff
        django_get_or_create = ('user',)

    user = SubFactory(UserFactory)

class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student
        django_get_or_create = ('user',)

    user = SubFactory(UserFactory)
