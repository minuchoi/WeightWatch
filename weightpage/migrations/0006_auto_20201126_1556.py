# Generated by Django 3.1.3 on 2020-11-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weightpage', '0005_auto_20201126_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='url',
            field=models.CharField(default='', max_length=30),
        ),
    ]