# Generated by Django 4.0.7 on 2023-04-06 18:32

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0161_cabling_cleanup'),
        ('extras', '0077_customlink_extend_text_and_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
                ('comments', models.TextField(blank=True)),
                ('device', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
