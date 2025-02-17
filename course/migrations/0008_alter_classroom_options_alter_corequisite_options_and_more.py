# Generated by Django 4.2 on 2025-01-29 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_rename_classroom_courseclassroom_classroom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'کلاس', 'verbose_name_plural': 'کلاس ها'},
        ),
        migrations.AlterModelOptions(
            name='corequisite',
            options={'verbose_name': 'هم نیاز', 'verbose_name_plural': 'هم نیاز ها ها'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'درس', 'verbose_name_plural': 'درس ها'},
        ),
        migrations.AlterModelOptions(
            name='courseclassroom',
            options={'verbose_name': 'کلاس درس', 'verbose_name_plural': 'کلاس درس ها'},
        ),
        migrations.AlterModelOptions(
            name='courseschedule',
            options={'verbose_name': 'مشخصات درس', 'verbose_name_plural': 'مشخصات درس ها'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'نام دانشکده', 'verbose_name_plural': 'نام دانشکده ها'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': ' انتخاب واحد', 'verbose_name_plural': '  انتخاب واحد درس ها'},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'مدرس', 'verbose_name_plural': 'مدرس ها'},
        ),
        migrations.AlterModelOptions(
            name='prerequisite',
            options={'verbose_name': 'پیش نیاز', 'verbose_name_plural': 'پیش نیاز ها'},
        ),
        migrations.AlterModelOptions(
            name='weeklyschedule',
            options={'verbose_name': 'برنامه هفتگی', 'verbose_name_plural': 'برنامه های هفتگی '},
        ),
    ]
