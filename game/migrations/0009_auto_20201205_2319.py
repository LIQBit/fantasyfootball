# Generated by Django 3.1 on 2020-12-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20201205_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kicker',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='quarterback',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='runningback',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='tightend',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='widereceiver',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
