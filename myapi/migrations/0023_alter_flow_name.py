# Generated by Django 5.0.3 on 2024-06-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0022_forummessage_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
