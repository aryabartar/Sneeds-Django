# Generated by Django 2.2.3 on 2020-03-23 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200322_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldproduct',
            name='sold_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
