# Generated by Django 4.2 on 2023-04-22 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_book_published_date_book_publishing_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='number_of_chapters',
            new_name='chapters',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number_of_pages',
            new_name='pages',
        ),
    ]