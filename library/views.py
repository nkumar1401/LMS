from django.shortcuts import render
from rest_framework.decorators import api_view ,APIView
from rest_framework.decorators  import permission_classes 
from rest_framework.permissions import IsAuthenticated   ,AllowAny
# from rest_framework.
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



@api_view(['GET'])
@permission_classes([AllowAny])
def allbook(request):
    author=request.GET.get('author')
    genre=request.GET.get('genre')
    book=Book.objects.all()
    if author:
        books=book.filter(author=author)
    if genre:
        books=book.filter(genre__name__icontain=genre)    
    serializer=BookSerializer(book.distinct(),many=True)
    return Response(serializer.data ,status=status.HTTP_200_OK)

from .permissions import *
@api_view(['POST'])
@permission_classes([IsAuthenticated ,Islibrarian])
def createauthor(request):
    serializers=AuthorSerializer(data=request.data)
    if serializers.is_valid():
        author=serializers.save()
        return Response(AuthorSerializer(author).data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])    
@permission_classes([AllowAny])
def registeruser(request):
    serializers=RegisterSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


    