# Generated by Django 3.2.7 on 2021-11-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_new_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='description',
        ),
        migrations.AddField(
            model_name='new',
            name='desciption',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
