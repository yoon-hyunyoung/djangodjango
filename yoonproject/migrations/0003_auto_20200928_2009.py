# Generated by Django 3.1.1 on 2020-09-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoonproject', '0002_auto_20200928_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epl',
            name='draw',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='epl',
            name='lose',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='epl',
            name='score',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='epl',
            name='win',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
