# Generated by Django 4.1.2 on 2023-02-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
