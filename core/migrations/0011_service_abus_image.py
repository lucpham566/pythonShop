# Generated by Django 3.2.7 on 2021-11-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211118_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='abus_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]