# Generated by Django 2.2.3 on 2019-07-27 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=90)),
                ('link', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]