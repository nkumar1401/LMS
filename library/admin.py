from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Book)
class Bookadmin(admin.ModelAdmin):
    list_display=['title','author']
@admin.register(Author)
class Authoradmin(admin.ModelAdmin):    
    list_display=['name','bio']
@admin.register(Genre)
class Genreadmin(admin.ModelAdmin):
    list_display=['name']
@admin.register(BorrowRequest)
class BorrowRequestadmin(admin.ModelAdmin):
    list_display=['book','user','status','requested_at']
    list_filter=['status']
    search_fields=['book__title','user__username']
    list_editable=['status']
@admin.register(BookReview)
class BookReviewadmin(admin.ModelAdmin):    
    list_display=['user','book','rating','created_at']
    list_filter=['rating']
    search_fields=['user__username','book__title']
    list_editable=['rating']
@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display=['username','role']
    list_filter=['role']
    search_fields=['username','email']
    