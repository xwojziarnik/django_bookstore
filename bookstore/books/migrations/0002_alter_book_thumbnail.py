# Generated by Django 4.0.4 on 2022-05-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.URLField(blank=True, verbose_name='URL to thumbnail of the book'),
        ),
    ]