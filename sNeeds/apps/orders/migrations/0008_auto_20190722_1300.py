# Generated by Django 2.2.3 on 2019-07-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190721_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created')], default='created', max_length=256),
        ),
    ]