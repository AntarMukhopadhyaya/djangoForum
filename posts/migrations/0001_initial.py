# Generated by Django 4.1.2 on 2023-01-26 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(default='', max_length=60)),
                ('category_description', models.TextField()),
                ('category_thumbnail', models.ImageField(null=True, upload_to='thumbnails/category')),
                ('category_slug', models.SlugField(null=True, unique=True)),
                ('category_post_number', models.PositiveBigIntegerField(default=0)),
                ('category_created_at', models.DateTimeField(auto_now_add=True)),
                ('category_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category_tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
