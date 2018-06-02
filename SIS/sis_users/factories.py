from factory import DjangoModelFactory, lazy_attribute, SubFactory
from django.contrib.auth.models import User
import faker
faker = faker.Factory.create()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = lazy_attribute(lambda x: faker.user_name())
    first_name = lazy_attribute(lambda x: faker.first_name())
    last_name = lazy_attribute(lambda x: faker.last_name())
    email = lazy_attribute(lambda x: faker.email())
    password = lazy_attribute(lambda x: faker.password())
