from django.test import TestCase
from django.contrib.auth.models import User
from sis_users.factories import (
    AdminStateFactory,
    StaffStateFactory,
    StudentStateFactory,
    UserFactory
)
from class_groups.factories import SetFactory

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

    def test_staff_model(self):
        '''
            Same process as Admin model, but with the Staff model instead.
        '''
        # create a staff state
        state = StaffStateFactory()
        # create a user
        user = UserFactory(email=state.email)
        # retrieve that user from the db
        user_from_db = User.objects.get(
            email=state.email
        )
        # check the instance has a 'staff' attribute
        assert hasattr(user_from_db, 'staff')

    def test_student_instance(self):
        '''
            StudentStateFactory creates a state, then a UserFactory creates
            a user using the same email address.
            The user should have a link with a student instance, with the same
            attributes and values as the user from the database.
        '''

        # create a class group
        class_group = SetFactory()
        # create a student state with the same class attributes
        state = StudentStateFactory(
            year=class_group.band.year.value,
            band=class_group.band.value,
            set=class_group.value
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
        self.assertEqual(
            student.class_group.band.year.value,
            state.year
        )
        self.assertEqual(
            student.class_group.band.value,
            state.band
        )
        self.assertEqual(
            student.class_group.value,
            state.set
        )

