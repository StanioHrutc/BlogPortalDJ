# Generated by Django 2.2.3 on 2019-07-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_is_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=70),
        ),
    ]
