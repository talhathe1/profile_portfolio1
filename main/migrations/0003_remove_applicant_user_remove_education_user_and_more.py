# Generated by Django 4.2.4 on 2023-08-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='education',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.applicant'),
        ),
        migrations.AddField(
            model_name='job',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.applicant'),
        ),
        migrations.AddField(
            model_name='project',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.applicant'),
        ),
        migrations.AddField(
            model_name='skill',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.applicant'),
        ),
    ]
