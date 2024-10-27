from django.db import models

# Create your models here.
class car(models.Model) :
    title = models.TextField(max_length=250)
    year = models.IntegerField( max_length = 4 , null = True)
    color= models.TextField(max_length=20, null=True)

    def __str__(self):
        return f" {self.title} - {self.year}"

class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str_(selft):
        return selft.name
    
class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField() # Fecha de publicación
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # Here we are defining a one-to-many relationship: a book has only one publisher, but a publisher can have many books.

    def __str__(self):
        return 