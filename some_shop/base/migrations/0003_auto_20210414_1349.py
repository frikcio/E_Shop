# Generated by Django 3.1.7 on 2021-04-14 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_temporarytoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ['name']},
        ),
    ]