# Generated by Django 5.0.6 on 2024-05-29 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0002_faculty_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.faculty')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.subject')),
            ],
        ),
    ]
