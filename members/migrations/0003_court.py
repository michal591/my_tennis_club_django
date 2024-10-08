# Generated by Django 5.1.1 on 2024-09-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('is_occupied', models.BooleanField(default=False)),
                ('time_of_occupation', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField()),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
