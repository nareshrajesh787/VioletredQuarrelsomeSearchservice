# Generated by Django 5.1.2 on 2024-12-30 21:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_assignment_uploaded_rubric_assignment_rubric_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='num_criteria',
            field=models.PositiveSmallIntegerField(default=4, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
    ]
