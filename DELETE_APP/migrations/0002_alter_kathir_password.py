# Generated by Django 3.2.4 on 2021-07-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DELETE_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kathir',
            name='password',
            field=models.IntegerField(max_length=100),
        ),
    ]
