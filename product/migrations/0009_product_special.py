# Generated by Django 3.2.7 on 2021-11-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='special',
            field=models.BooleanField(default=True),
        ),
    ]
