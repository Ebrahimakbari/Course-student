# Generated by Django 4.2 on 2025-01-29 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_student_national_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربر ها'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'دانشجو', 'verbose_name_plural': 'دانشجو ها'},
        ),
        migrations.AlterModelOptions(
            name='userlevel',
            options={'verbose_name': 'سطح کاربر ', 'verbose_name_plural': 'سطح های کاربر '},
        ),
    ]
