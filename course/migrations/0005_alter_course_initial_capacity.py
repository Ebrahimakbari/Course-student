# Generated by Django 4.2 on 2025-01-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_initial_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='initial_capacity',
            field=models.IntegerField(),
        ),
    ]
