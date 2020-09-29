# Generated by Django 3.1.1 on 2020-09-29 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoonproject', '0009_auto_20200929_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epl',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoonproject.eplstatusgroup'),
        ),
        migrations.AlterField(
            model_name='epl',
            name='status',
            field=models.CharField(choices=[('EPL', 'EPL'), ('EFL', 'EFL'), ('리그1', '리그1')], max_length=50),
        ),
    ]