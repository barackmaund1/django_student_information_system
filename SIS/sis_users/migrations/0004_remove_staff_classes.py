# Generated by Django 2.0.5 on 2018-06-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis_users', '0003_staff_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='classes',
        ),
    ]
