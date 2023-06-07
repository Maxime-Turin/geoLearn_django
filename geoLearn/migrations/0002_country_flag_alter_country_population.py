# Generated by Django 4.2.2 on 2023-06-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoLearn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.IntegerField(blank=True),
        ),
    ]
