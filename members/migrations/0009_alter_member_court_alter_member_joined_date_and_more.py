# Generated by Django 5.1.1 on 2024-09-17 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0003_delete_reservation'),
        ('members', '0008_member_court'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='court',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='members', to='courts.court'),
        ),
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
