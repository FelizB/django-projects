# Generated by Django 4.1.1 on 2022-10-12 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_rename_firt_name_patient_first_name_patient_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
