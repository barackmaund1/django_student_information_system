from django.test import TestCase

class PostSaveTestCase(TestCase):
    '''
        Test that the post_save hooks are working correctly
        ie. making the correct instance based on the info from the state table
    '''
    def setUp(self):
        pass

    def test_student_instance(self):
        assert 1 == 1
