# Generated by Django 3.1.7 on 2022-01-12 12:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_usertype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserType',
            new_name='UserProfile',
        ),
    ]
