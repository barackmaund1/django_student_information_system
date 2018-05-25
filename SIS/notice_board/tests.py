from django.test import TestCase
from notice_board.factories import AnnouncementFactory
from notice_board.models import Announcement

class AnnouncementTestCase(TestCase):
    def test_announcement_information(self):
        ''' check announcement was created correctly '''
        announcement = AnnouncementFactory()
        return_announcement = Announcement.objects.get(pk=announcement.pk)

        for key, value in announcement.__dict__.items():
            if key != '_state':
                self.assertEqual(
                    getattr(return_announcement, key),
                    value
                )