from django.urls import path
from .views import *

urlpatterns=[
    path('allbook/',allbook,name='allbook'),
    path('createauthor/',createauthor,name='createauthor'),
    path('registeruser/',registeruser,name='registeruser')

]