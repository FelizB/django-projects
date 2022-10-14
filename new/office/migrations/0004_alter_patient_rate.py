# Generated by Django 4.1.1 on 2022-10-12 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_rename_second_name_patient_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='rate',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)]),
        ),
    ]
