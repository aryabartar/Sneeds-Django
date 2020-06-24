# Generated by Django 2.2.3 on 2020-06-18 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicProducts', '0003_auto_20200524_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoomLink',
            fields=[
                ('roomlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basicProducts.RoomLink')),
            ],
            bases=('basicProducts.roomlink',),
        ),
        migrations.CreateModel(
            name='WebinarRoomLink',
            fields=[
                ('roomlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basicProducts.RoomLink')),
            ],
            bases=('basicProducts.roomlink',),
        ),
        migrations.AddField(
            model_name='roomlink',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]