# Generated by Django 4.0.3 on 2022-03-27 15:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_article_photo_presentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo_presentation',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]