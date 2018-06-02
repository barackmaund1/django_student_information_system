from factory import DjangoModelFactory, lazy_attribute, SubFactory
from django.contrib.auth.models import User
import faker
from random import choice

from sis_users.models import Staff, Student, UserState
from sis_users.choices import CLASS_CHOICES, YEAR_GROUP_CHOICES

faker = faker.Factory.create()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = lazy_attribute(lambda x: faker.user_name())
    first_name = lazy_attribute(lambda x: faker.first_name())
    last_name = lazy_attribute(lambda x: faker.last_name())
    email = lazy_attribute(lambda x: faker.email())
    password = lazy_attribute(lambda x: faker.password())

class StaffStateFactory(DjangoModelFactory):
    class Meta:
        model = UserState

    email_address = lazy_attribute(lambda x: faker.email())
    staff = True

class StudentStateFactory(DjangoModelFactory):
    class Meta:
        model = UserState

    email_address = lazy_attribute(lambda x: faker.email())
    staff = False
    year_group = lazy_attribute(lambda x: choice([c[0] for c in YEAR_GROUP_CHOICES]))
    class_group = lazy_attribute(lambda x: choice([c[0] for c in CLASS_CHOICES]))
