# Generated by Django 2.0.5 on 2019-06-22 14:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('movies', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]