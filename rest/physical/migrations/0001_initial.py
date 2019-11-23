# Generated by Django 2.2.7 on 2019-11-23 18:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
                ('sequence', models.PositiveIntegerField(db_index=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxes', to='metadata.Collection')),
            ],
            options={
                'ordering': ['sequence'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
                ('sequence', models.PositiveIntegerField(db_index=True)),
            ],
            options={
                'ordering': ['sequence'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
                ('sequence', models.PositiveIntegerField(db_index=True)),
                ('fulltext', models.TextField(blank=True, editable=False)),
                ('pdf', models.CharField(max_length=800, null=True)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='physical.Bundle')),
            ],
            options={
                'ordering': ['sequence'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
                ('sequence', models.PositiveIntegerField(db_index=True)),
                ('tiff', models.CharField(max_length=800, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='physical.Document')),
            ],
            options={
                'ordering': ['sequence'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(default=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False), max_length=1000, null=True)),
                ('sequence', models.PositiveIntegerField(db_index=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='physical.Box')),
            ],
            options={
                'ordering': ['sequence'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bundle',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundles', to='physical.Folder'),
        ),
    ]
