# Generated by Django 3.1.3 on 2020-11-30 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weightpage', '0006_auto_20201126_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weight',
            name='time',
            field=models.TimeField(),
        ),
    ]