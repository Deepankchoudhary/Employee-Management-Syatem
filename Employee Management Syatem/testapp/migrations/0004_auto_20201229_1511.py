# Generated by Django 3.1.1 on 2020-12-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='added_by',
            field=models.CharField(max_length=40),
        ),
    ]