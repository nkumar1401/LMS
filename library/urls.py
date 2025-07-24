from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('books',BookListView,basename='books')

urlpatterns=[
    path('allbook/',allbook,name='allbook'),
    path('createauthor/',createauthor,name='createauthor'),
    path('registeruser/',registeruser,name='registeruser'),
    path('', include(router.urls)),

]