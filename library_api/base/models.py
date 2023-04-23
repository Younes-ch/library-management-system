from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publishing_year = models.IntegerField()
    pages = models.IntegerField()
    chapters = models.IntegerField()

    def __str__(self):
        return self.title
