# Generated by Django 2.0.5 on 2018-10-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20181008_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklet',
            name='slug',
            field=models.SlugField(default=None, null=True),
        ),
    ]