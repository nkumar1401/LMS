from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT='STUDENT','student'
        LIBRARIAN='LIBRARIAN','librarian'
    role=models.CharField(max_length=10, choices=Role.choices,default=Role.STUDENT) 

class Author(models.Model):
    name=models.CharField(max_length=50)
    bio=models.TextField()

class Genre(models.Model):
    name=models.CharField(max_length=50)

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    genres=models.ManyToManyField(Genre,related_name='books')
    ISBN=models.IntegerField(unique=True)
    available_copies=models.PositiveIntegerField()
    total_copies=models.PositiveIntegerField()

class BorrowRequest(models.Model):
    class Status(models.TextChoices):
        PENDING='PENDING','pending'
        APPROVED='APPROVED','approved'
        REJECTED='REJECTED','rejected'
        RETURNED='RETURNED','returned'
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowrequest')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrowrequest')
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    requested_at=models.DateField(auto_now_add=True)
    approved_at=models.DateField(blank=True,null=True)
    returned_at=models.DateField(blank=True,null=True)


class BookReview(models.Model):
    class Ratingchoices(models.IntegerChoices):
            ONE=1,'1'
            TWO=2,'2'
            THREE=3,'3'
            FOUR=4,'4'
            FIVE=5,'5'
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookreviews')
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='bookreviews')
    rating=models.IntegerField(choices=Ratingchoices.choices)
    comment=models.TextField()
    created_at=models.DateField(auto_now_add=True)