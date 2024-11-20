# Generated by Django 5.1 on 2024-11-17 01:50

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'ATTENDANCE'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'CLASS'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': 'GRADE'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'STUDENT PROFILE'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'SUBJECT'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'TEACHER'},
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Father No.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Guardian Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Mother No.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_photo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='media'), upload_to='media', verbose_name='Profile Photo'),
        ),
        migrations.AlterModelTable(
            name='attendance',
            table='ATTENDANCE',
        ),
        migrations.AlterModelTable(
            name='class',
            table='CLASS',
        ),
        migrations.AlterModelTable(
            name='grade',
            table='GRADE',
        ),
        migrations.AlterModelTable(
            name='student',
            table='STUDENT PROFILE',
        ),
        migrations.AlterModelTable(
            name='subject',
            table='SUBJECT',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='TEACHER',
        ),
    ]