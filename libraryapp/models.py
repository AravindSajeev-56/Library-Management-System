from django.db import models

# Create your models here.
class books(models.Model):
    book_name= models.CharField(primary_key=True,max_length=70)
    book_author=models.CharField(max_length=30)
    book_type=models.CharField(max_length=30)
    details=models.TextField(max_length=100)
    bookid=models.CharField(max_length=10)
    availability=models.CharField(max_length=10)
    def __str__(self):
        return self.book_name

class Bookingbooks(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    place = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    bookid = models.CharField(max_length=10)
    def __str__(self):
        return self.name


