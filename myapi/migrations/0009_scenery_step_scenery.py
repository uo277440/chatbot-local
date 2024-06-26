# Generated by Django 5.0.3 on 2024-05-05 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_alter_flow_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'scenery',
            },
        ),
        migrations.AddField(
            model_name='step',
            name='scenery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='scenery', to='myapi.scenery'),
            preserve_default=False,
        ),
    ]
