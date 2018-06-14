from django.core.management import BaseCommand
import os
from random import choice
from sis_users.factories import (
    AdminStateFactory,
    StaffStateFactory,
    StudentStateFactory,
    AdminFactory,
    StaffFactory,
    StudentFactory
)
from class_groups.models import Set

class Command(BaseCommand):
    def handle(self, *args, **options):
        admin_email = os.environ['ADMIN_EMAIL']
        staff_email = os.environ['STAFF_EMAIL']
        student_email = os.environ['STUDENT_EMAIL']

        # create three states
        admin_state = AdminStateFactory(email=admin_email)
        staff_state = StaffStateFactory(email=staff_email)
        student_state = StudentStateFactory(email=student_email)

        # print out what's happened
        self.stdout.write('3 states created.')
        self.stdout.write(f'Admin: {admin_state}')
        self.stdout.write(f'Staff: {staff_state}')
        self.stdout.write(f'Student: {student_state}')


