# Generated by Django 4.2 on 2025-01-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_student_max_units_alter_student_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='national_id',
            field=models.IntegerField(max_length=10),
        ),
    ]
