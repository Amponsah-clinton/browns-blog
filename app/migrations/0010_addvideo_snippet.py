# Generated by Django 4.2 on 2023-07-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_addvideo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='addvideo',
            name='snippet',
            field=models.CharField(default='Hi', max_length=200),
        ),
    ]
