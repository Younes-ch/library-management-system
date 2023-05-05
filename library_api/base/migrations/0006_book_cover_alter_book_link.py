# Generated by Django 4.2 on 2023-05-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_book_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
