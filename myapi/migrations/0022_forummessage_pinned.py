# Generated by Django 5.0.3 on 2024-05-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0021_mark_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='forummessage',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]