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
from class_groups.models import ClassGroup

class Command(BaseCommand):
    def handle(self, *args, **options):
        admin_email = os.environ['ADMIN_EMAIL']
        staff_email = os.environ['STAFF_EMAIL']
        student_email = os.environ['STUDENT_EMAIL']

        # create admin state
        state = AdminStateFactory(email=admin_email)
        # create admin user
        admin = AdminFactory(user__email=state.email)

        # same for staff
        state = StaffStateFactory(email=staff_email)
        staff = StaffFactory(user__email=state.email)

        # same for student
        state = StudentStateFactory(email=student_email)
        student = StudentFactory(user__email=state.email)

        # assign some random class to the student
        classes = list(ClassGroup.objects.all())
        # random class group
        class_group = choice(classes)
        # assign it to the student
        student.class_group = class_group
        # save the student
        student.save()

        # print out what's happened
        self.stdout.write('3 users created.')
        self.stdout.write(f'Admin: {admin}')
        self.stdout.write(f'Staff: {staff}')
        self.stdout.write(f'Student: {student}')
        self.stdout.write(f'Class: {student.class_group}')


