# Generated by Django 4.1.2 on 2023-03-11 10:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_post_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
