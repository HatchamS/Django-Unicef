# Generated by Django 4.0.3 on 2022-03-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_photo_presentation_alter_article_contenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo_presentation',
            field=models.ImageField(null=True, upload_to='CoverArticle'),
        ),
    ]
