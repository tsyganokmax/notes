from django.db import models

#class Author(models.)

class Book(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name


