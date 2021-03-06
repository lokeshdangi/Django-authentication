# Generated by Django 2.0.5 on 2018-05-09 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180509_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserAddress',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserEmail',
            field=models.EmailField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserEmailVerified',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserFirstName',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserIP',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserLastName',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserPhone',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
