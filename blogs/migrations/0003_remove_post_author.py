# Generated by Django 3.2 on 2021-05-11 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
