from factory import DjangoModelFactory
from factory import Faker
from notice_board.models import Announcement

class AnnouncementFactory(DjangoModelFactory):
    class Meta:
        model = Announcement

    header = Faker('text').generate(extra_kwargs={'max_nb_chars': 50})
    body_text = Faker('text').generate(extra_kwargs={'max_nb_chars': 500})
