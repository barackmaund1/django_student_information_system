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

class BasePostSaveTestCase(TestCase):
    def setUp(self):
        '''
            Setup generic stuff here that will be common for all test cases
        '''
        state_class = self.get_state_class()

        if state_class.__name__ == 'StudentStateFactory':
            set = SetFactory()
            self.state = state_class(
                year=set.band.year.value,
                band=set.band.value,
                set=set.value
            )
        else:
            self.state = state_class()
        # create a user
        user = UserFactory(email=self.state.email)
        # get the user from the database
        self.user = User.objects.get(
            email=self.state.email
        )

    def get_state_class(self):
        if not hasattr(self, 'state_class'):
            raise self.fail('Must define a state_class for each subclass.')
        else:
            return self.state_class

class AdminPostSaveTestCase(BasePostSaveTestCase):
    state_class = AdminStateFactory

    def test_admin_post_save(self):
        # check user has an admin attr
        self.assertTrue(hasattr(self.user, 'admin'))
        # also a staff attr
        self.assertTrue(hasattr(self.user, 'staff'))
        # but not a student attr
        self.assertFalse(hasattr(self.user, 'student'))

class StaffPostSaveTestCase(BasePostSaveTestCase):
    state_class = StaffStateFactory

    def test_staff_post_save(self):
        # check user has a staff attr
        self.assertTrue(hasattr(self.user, 'staff'))
        # but not an admin attr
        self.assertFalse(hasattr(self.user, 'admin'))
        # or a student attr
        self.assertFalse(hasattr(self.user, 'student'))

class StudentPostSaveTestCase(BasePostSaveTestCase):
    state_class = StudentStateFactory

    def test_student_post_save(self):
        # test user has a student attr
        self.assertTrue(hasattr(self.user, 'student'))
        # but not an admin attr
        self.assertFalse(hasattr(self.user, 'admin'))
        # or a staff attr
        self.assertFalse(hasattr(self.user, 'staff'))

        # get the student instance
        student = self.user.student
        # check that the student is in the right class as the state said it should be
        self.assertEqual(
            student.set.band.year.value,
            self.state.year
        )
        self.assertEqual(
            student.set.band.value,
            self.state.band
        )
        self.assertEqual(
            student.set.value,
            self.state.set
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
