# Generated by Django 3.1.1 on 2021-01-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_friend_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='friend',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
