# Generated by Django 2.0.5 on 2018-05-09 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180509_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='UserEmailVerified',
        ),
    ]
