# Generated by Django 3.2.5 on 2024-04-03 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 3, 6, 32, 50, 960790, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default=datetime.datetime(2024, 4, 3, 6, 32, 57, 973929, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
