# Generated by Django 3.1.7 on 2022-01-12 13:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_auto_20220112_1222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserType',
        ),
    ]
