# Generated by Django 2.2.3 on 2019-07-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
