from django.test import TestCase, Client
from django.urls import reverse
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

class BaseAccessMessageMixinTestCase(TestCase):
    def setUp(self):
        '''
            Setup generic stuff here that will be common for all test cases
        '''
        # create a client
        self.client = Client()
        if self.get_state_class():
            # create some credentials
            self.credentials = {
                'email': 'test@example.com',
                'username': 'test_user',
                'password': '123456'
            }

            state_class = self.get_state_class()
            if state_class.__name__ == 'StudentStateFactory':
                set = SetFactory()
                state = state_class(
                    email=self.credentials['email'],
                    year=set.band.year.value,
                    band=set.band.value,
                    set=set.value
                )
            else:
                state = state_class(
                    email=self.credentials['email']
                )
            # create a user
            user = UserFactory(**self.credentials)
            # set the user's password
            user.set_password(self.credentials['password'])
            # save the user
            user.save()
            # get the user from the database
            self.user = User.objects.get(
                email=self.credentials['email']
            )

    def access_test(self, url_to_reverse, status_code):
        response = self.client.get(reverse(url_to_reverse))
        self.assertEqual(response.status_code, status_code)

    def get_state_class(self):
        if not hasattr(self, 'state_class'):
            raise self.fail('Must define a state_class for each subclass.')
        else:
            return self.state_class

    def login_test(self):
        logged_in = self.client.login(**self.credentials)
        self.assertTrue(logged_in)

class TestAdminAccess(BaseAccessMessageMixinTestCase):
    state_class = AdminStateFactory

    def test_admin_access(self):
        # check the user has an admin attribute
        self.assertTrue(hasattr(self.user, 'admin'))
        # and a staff
        self.assertTrue(hasattr(self.user, 'staff'))
        # but not a student
        self.assertFalse(hasattr(self.user, 'student'))

        # test logging in
        self.login_test()

        self.access_test('home:home-page', 200)
        self.access_test('sis_users:admin-list', 200)
        self.access_test('sis_users:staff-list', 200)
        self.access_test('sis_users:student-list', 200)

class TestStaffAccess(BaseAccessMessageMixinTestCase):
    state_class = StaffStateFactory

    def test_staff_access(self):
        # check user has staff attr
        self.assertTrue(hasattr(self.user, 'staff'))
        # check they don't have admin attr
        self.assertFalse(hasattr(self.user, 'admin'))
        # or student attr
        self.assertFalse(hasattr(self.user, 'student'))

        # test logging in
        self.login_test()

        self.access_test('home:home-page', 200)
        self.access_test('sis_users:admin-list', 302)
        self.access_test('sis_users:staff-list', 200)
        self.access_test('sis_users:student-list', 200)

class TestStudentAccess(BaseAccessMessageMixinTestCase):
    state_class = StudentStateFactory

    def test_student_access(self):
        # check user has student attr
        self.assertTrue(hasattr(self.user, 'student'))
        # check they don't have admin attr
        self.assertFalse(hasattr(self.user, 'admin'))
        # or staff attr
        self.assertFalse(hasattr(self.user, 'staff'))

        # test logging in
        self.login_test()

        self.access_test('home:home-page', 200)
        self.access_test('sis_users:admin-list', 302)
        self.access_test('sis_users:staff-list', 302)
        self.access_test('sis_users:student-list', 200)

class TestAnonymousAccess(BaseAccessMessageMixinTestCase):
    state_class = None

    def test_anon_access(self):
        # no need to test for admin, staff or student attrs
        # or to check login

        # this will succeed
        self.access_test('home:home-page', 200)
        # rest will be redirected
        self.access_test('sis_users:admin-list', 302)
        self.access_test('sis_users:staff-list', 302)
        self.access_test('sis_users:student-list', 302)
