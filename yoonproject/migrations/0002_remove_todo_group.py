# Generated by Django 3.1.1 on 2020-09-23 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoonproject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='group',
        ),
    ]