# Generated by Django 3.2.7 on 2021-11-18 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 13, 33, 23, 275187)),
        ),
    ]
