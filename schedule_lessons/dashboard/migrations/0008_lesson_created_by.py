# Generated by Django 2.0.6 on 2018-08-01 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_remove_lesson_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
