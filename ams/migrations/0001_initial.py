# Generated by Django 5.0.6 on 2024-05-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('student_image', models.ImageField(upload_to='images')),
                ('student_roll', models.IntegerField()),
                ('student_year', models.IntegerField()),
                ('student_email', models.EmailField(max_length=254)),
                ('student_phone', models.CharField(max_length=255)),
                ('student_address', models.TextField()),
            ],
        ),
    ]