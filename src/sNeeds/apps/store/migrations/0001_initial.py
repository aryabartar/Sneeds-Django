# Generated by Django 2.2.3 on 2020-02-14 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customAuth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlotSale',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.Product')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customAuth.ConsultantProfile')),
            ],
            options={
                'abstract': False,
            },
            bases=('store.product',),
        ),
        migrations.CreateModel(
            name='SoldTimeSlotSale',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.Product')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('used', models.BooleanField(default=False)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customAuth.ConsultantProfile')),
                ('sold_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('store.product',),
        ),
    ]