# Generated by Django 3.1.1 on 2020-09-29 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoonproject', '0008_auto_20200929_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epl',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoonproject.eplstatusgroup'),
        ),
    ]