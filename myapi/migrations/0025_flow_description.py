# Generated by Django 5.0.3 on 2024-06-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0024_alter_flow_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='flow',
            name='description',
            field=models.CharField(default='Bienvenido al flujo. Recuerda empezar saludando !', max_length=100),
        ),
    ]
