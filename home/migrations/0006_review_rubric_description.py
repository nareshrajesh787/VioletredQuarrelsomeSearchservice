# Generated by Django 5.1.2 on 2025-01-06 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_assignment_num_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rubric_description',
            field=models.JSONField(default=dict),
        ),
    ]