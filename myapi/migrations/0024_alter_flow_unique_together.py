# Generated by Django 5.0.3 on 2024-06-04 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0023_alter_flow_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='flow',
            unique_together={('name', 'scenery')},
        ),
    ]
