# Generated by Django 2.2.7 on 2019-11-23 18:06

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('physical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.FloatField(db_index=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physical.Document')),
            ],
        ),
        migrations.CreateModel(
            name='UserCreatedModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentCollection',
            fields=[
                ('usercreatedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='text.UserCreatedModel')),
                ('documents', models.ManyToManyField(related_name='document_collections', to='physical.Document')),
            ],
            options={
                'abstract': False,
            },
            bases=('text.usercreatedmodel',),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
                ('terms', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('documents', models.ManyToManyField(through='text.DocumentTopic', to='physical.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='documenttopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.Topic'),
        ),
        migrations.CreateModel(
            name='TopicModel',
            fields=[
                ('usercreatedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='text.UserCreatedModel')),
                ('n_topics', models.PositiveIntegerField()),
                ('created_model', models.BinaryField(blank=True, null=True)),
                ('document_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_models', to='text.DocumentCollection')),
            ],
            options={
                'abstract': False,
            },
            bases=('text.usercreatedmodel',),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='text.TopicModel'),
        ),
    ]