# Generated by Django 2.2.3 on 2019-07-21 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190720_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslotsale',
            name='sold_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
