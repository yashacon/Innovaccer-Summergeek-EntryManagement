# Generated by Django 2.2.7 on 2020-01-16 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100)),
                ('host_email', models.EmailField(max_length=254)),
                ('host_phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=100)),
                ('visitor_email', models.EmailField(max_length=254)),
                ('visitor_phone', models.IntegerField(max_length=10)),
                ('checkin', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('checkout', models.DateTimeField(blank=True)),
            ],
        ),
    ]
