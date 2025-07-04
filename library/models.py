from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator ,MaxValueValidator

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT='STUDENT','_STUDENT'
        LIBRARIAN="LIBRARIAN",'_LIBRARIAN'
    role=models.CharField(max_length=20,choices=Role.choices,default=Role.STUDENT)
    def __str__(self):
        return f'{self.username}--{self.role}'
    

    
class Author(models.Model):
    name=models.CharField(max_length=20)   
    bio=models.TextField()
    def __str__(self):
        return f'{self.name}--{self.bio}'

class Genre(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}' 

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    genre=models.ManyToManyField(Genre,related_name='books')
    isbn=models.CharField(max_length=20,unique=True)
    available_copies=models.PositiveIntegerField()
    total_copies=models.PositiveBigIntegerField()
    def __str__(self):
        return f'{self.title}'

class BorrowRequest(models.Model):
    class Status(models.TextChoices):
        PENDING='PENDING','pending'
        APPROVED='APPROVED','approved'
        REJECTED='REJECTED','rejected'
        RETURNED='RETURNED','returned'
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrow_requests')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrow_requests')
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    requested_at=models.DateField(auto_now_add=True)
    approved_at=models.DateField(blank=True,null=True)
    returned_at=models.DateField(blank=True,null=True)
    def __str__(self):
        return f'{self.book}'
class BookReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_reviews')
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='book_reviews')
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.book}'


