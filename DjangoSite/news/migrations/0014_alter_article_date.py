# Generated by Django 4.0.3 on 2022-06-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.CharField(default='04 Jun 2022', max_length=100),
        ),
    ]
