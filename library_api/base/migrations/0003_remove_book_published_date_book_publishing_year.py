# Generated by Django 4.2 on 2023-04-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_book_options_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_year',
            field=models.IntegerField(default=1990),
            preserve_default=False,
        ),
    ]
