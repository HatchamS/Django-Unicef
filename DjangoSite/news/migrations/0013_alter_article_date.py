# Generated by Django 4.0.3 on 2022-04-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.CharField(default='02 Apr 2022', max_length=100),
        ),
    ]
