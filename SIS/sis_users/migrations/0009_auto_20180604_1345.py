# Generated by Django 2.0.5 on 2018-06-04 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis_users', '0008_auto_20180602_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstate',
            old_name='email_address',
            new_name='email',
        ),
    ]
