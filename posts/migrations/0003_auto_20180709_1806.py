# Generated by Django 2.0 on 2018-07-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180709_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
