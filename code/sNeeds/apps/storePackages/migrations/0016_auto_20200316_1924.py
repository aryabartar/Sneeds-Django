# Generated by Django 2.2.3 on 2020-03-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storePackages', '0015_storepackage_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storepackage',
            name='total_price',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
