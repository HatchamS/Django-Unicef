# Generated by Django 4.0.3 on 2022-03-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.CharField(default='27 Mar 2022', max_length=100),
        ),
    ]
