from factory import DjangoModelFactory
from factory import lazy_attribute
from notice_board.models import Announcement
import faker

faker = faker.Factory.create()

class AnnouncementFactory(DjangoModelFactory):
    class Meta:
        model = Announcement

    # header = Faker('text').generate(extra_kwargs={'max_nb_chars': 50})
    header = lazy_attribute(lambda x: faker.text(max_nb_chars=50))
    # body_text = Faker('text').generate(extra_kwargs={'max_nb_chars': 500})
    body_text = lazy_attribute(lambda x: faker.text(max_nb_chars=500))
