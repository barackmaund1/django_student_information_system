from django.test import TestCase

from sis_users.factories import StudentStateFactory, StaffStateFactory, UserFactory
from sis_users.models import UserState
from django.contrib.auth.models import User

class PostSaveTestCase(TestCase):
    '''
        Test that the post_save hooks are working correctly
        ie. making the correct instance based on the info from the state table
    '''
    def test_student_instance(self):
        '''
            Create a student state in the database,
            then create a user with the same email address
            assert that the user has a student instance
            wtih the correct attributes (class_group, year_group)
        '''
        state = UserState.objects.create(
            email="some_test_email@example.com",
            staff=False,
            is_admin=False,
            year=10,
            band='V',
            set=1
        )
        # retrieve same user from User table
        user = User.objects.get(
            email=state.email
        )
        # assert it's got a relationship to student
        assert hasattr(user, 'student')
