# Generated by Django 2.1.7 on 2019-05-18 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='full_name',
            new_name='full_employee_name',
        ),
    ]
