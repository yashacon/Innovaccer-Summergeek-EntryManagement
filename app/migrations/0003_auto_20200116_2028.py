# Generated by Django 2.2.7 on 2020-01-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200116_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='checkout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
