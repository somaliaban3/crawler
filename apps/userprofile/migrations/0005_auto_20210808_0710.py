# Generated by Django 3.2.6 on 2021-08-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_rename_profile_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='baseLocation',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobDescription',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
