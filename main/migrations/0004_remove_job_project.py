# Generated by Django 4.2.4 on 2023-08-16 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_applicant_user_remove_education_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='project',
        ),
    ]
