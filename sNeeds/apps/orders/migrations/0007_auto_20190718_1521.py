# Generated by Django 2.2.3 on 2019-07-18 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190718_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]