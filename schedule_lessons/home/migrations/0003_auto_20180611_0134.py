# Generated by Django 2.0.6 on 2018-06-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180518_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(max_length=16),
        ),
    ]
