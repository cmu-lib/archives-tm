# Generated by Django 2.2.7 on 2019-11-28 00:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0004_auto_20191125_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicmodel',
            name='document_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), null=True, size=None),
        ),
    ]
