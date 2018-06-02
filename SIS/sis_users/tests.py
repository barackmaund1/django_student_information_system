from django.test import TestCase

from sis_users.factories import StudentStateFactory, StaffStateFactory, UserFactory

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
        state = StudentStateFactory()
        user = UserFactory(email=state.email_address)

        assert hasattr(user, 'student')
        student = user.student

        self.assertEqual(student.class_group, state.class_group)
        self.assertEqual(student.year_group, state.year_group)
