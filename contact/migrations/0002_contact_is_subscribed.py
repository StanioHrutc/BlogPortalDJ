# Generated by Django 2.2.3 on 2019-07-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]