# Generated by Django 5.1.2 on 2025-01-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_review_rubric_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]