# Generated by Django 3.1.1 on 2021-01-02 10:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0015_auto_20210102_1541'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friend',
            new_name='ProfileFriend',
        ),
    ]
