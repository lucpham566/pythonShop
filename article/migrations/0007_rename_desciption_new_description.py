# Generated by Django 3.2.7 on 2021-11-14 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_new_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='desciption',
            new_name='description',
        ),
    ]
