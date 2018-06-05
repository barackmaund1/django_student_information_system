from django.test import TestCase
from django.contrib.auth.models import User
from sis_users.factories import (
    AdminStateFactory,
    StaffStateFactory,
    StudentStateFactory,
    AdminFactory,
    StaffFactory,
    StudentFactory,
    UserFactory
)
from class_groups.factories import ClassGroupFactory

class PostSaveTestCase(TestCase):
    '''
        Test that the post_save hooks are working correctly
        ie. making the correct instance based on the info from the state table
    '''

    def test_admin_instance(self):
        '''
            AdminStateFactory creates a state, then a UserFactory creates a
            user using the same email address.
            The user should have an admin instance attached, currently there
            are no attribute values to check, until more functionality is
            given to the Admin model.
        '''
        # create an admin state
        state = AdminStateFactory()
        # create a user
        user = UserFactory(email=state.email)
        # retrieve the same user from the db
        user_from_db = User.objects.get(
            email=state.email
        )
        # check the instance has an 'admin' attribute
        assert hasattr(user_from_db, 'admin')

    def test_student_instance(self):
        '''
            StudentStateFactory creates a state, then a UserFactory creates
            a user using the same email address.
            The user should have a link with a student instance, with the same
            attributes and values as the user from the database.
        '''

        # create a class group
        class_group = ClassGroupFactory()
        # create a student state with the same class attributes
        state = StudentStateFactory(
            year=class_group.year,
            band=class_group.band,
            set=class_group.set
        )
        # create a user with the same email as the state
        user = UserFactory(email=state.email)
        # get the user from the database
        user_from_db = User.objects.get(
            email=state.email
        )
        # assert it has a student instance
        assert hasattr(user_from_db, 'student')
        # get the student instance
        student = user.student
        # check the student has a class_group instance
        assert hasattr(student, 'class_group')
        # check the attributes are equal to the state
        self.assertEqual(student.class_group.year, state.year)
        self.assertEqual(student.class_group.band, state.band)
        self.assertEqual(student.class_group.set, state.set)

