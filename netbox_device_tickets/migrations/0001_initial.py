# Generated by Django 4.1.5 on 2023-04-10 12:40

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0084_staging'),
        ('dcim', '0167_module_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
                ('creator', models.CharField(blank=True, max_length=100, null=True)),
                ('executor', models.CharField(blank=True, max_length=100, null=True)),
                ('start', models.DateTimeField(max_length=100)),
                ('end', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True)),
                ('device', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
