# Generated by Django 3.1.7 on 2021-03-26 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 13, 15, 7, 825363, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='returnmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 13, 15, 7, 826362, tzinfo=utc)),
        ),
    ]