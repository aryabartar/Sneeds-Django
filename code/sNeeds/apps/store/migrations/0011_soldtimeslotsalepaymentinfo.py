# Generated by Django 2.2.3 on 2020-06-07 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200520_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldTimeSlotSalePaymentInfo',
            fields=[
            ],
            options={
                'verbose_name_plural': 'SoldTimeSlotSale Payment Infos',
                'proxy': True,
                'verbose_name': 'SoldTimeSlotSale Payment Info',
                'indexes': [],
                'constraints': [],
            },
            bases=('store.soldtimeslotsale',),
        ),
    ]
