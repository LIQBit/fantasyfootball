# Generated by Django 3.1 on 2020-11-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kicker',
        ),
        migrations.DeleteModel(
            name='Quarterback',
        ),
        migrations.DeleteModel(
            name='Runningback',
        ),
        migrations.DeleteModel(
            name='Tightend',
        ),
        migrations.DeleteModel(
            name='Widereceiver',
        ),
    ]
