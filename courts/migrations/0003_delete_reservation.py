# Generated by Django 5.1.1 on 2024-09-17 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_reservation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
