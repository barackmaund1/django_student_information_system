from django.test import TestCase, Client
from notice_board.factories import AnnouncementFactory
from django.urls import reverse

# Create your tests here.

class HomeTestCase(TestCase):
    def setUp(self):
        # create a list of five announcements
        self.announcements = [AnnouncementFactory() for _ in range(5)]
        self.client = Client()

    def test_announcements_are_present(self):
        ''' Test that the announcements created in setup appear in the response '''
        # get a response from the home page
        response = self.client.get(reverse('home-page'))
        # pull out the announcements from the response
        announcements_from_response = response.context['announcements']
        # assert that the number of announcements in the response
        # match the number of announcements that were created
        self.assertCountEqual(
            self.announcements,
            announcements_from_response
        )

        # loop backwards through the announcements from the response
        # because they are sorted in reverse chronological order by the view
        for c, announcement in enumerate(reversed(announcements_from_response)):
            # assert that the created times are the time
            self.assertEqual(
                announcement.created,
                self.announcements[c].created
            )
            # assert that the headers are the same
            self.assertEqual(
                announcement.header,
                self.announcements[c].header
            )
            # assert that the body text is the same
            self.assertEqual(
                announcement.body_text,
                self.announcements[c].body_text
            )

    def test_page_title(self):
        response = self.client.get(reverse('home-page'))
        page_title = response.context['page_title']
        self.assertEqual(
            page_title,
            'home page'
        )
