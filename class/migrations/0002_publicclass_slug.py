# Generated by Django 2.1.3 on 2019-02-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicclass',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
