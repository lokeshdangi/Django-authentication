# Generated by Django 2.0.5 on 2018-05-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20180509_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserEmail',
            field=models.EmailField(max_length=256, unique=True),
        ),
    ]
