# Generated by Django 5.2 on 2025-05-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='description',
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
