from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.password_validation import validate_password
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password1=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=User
        fields=('username','role','password','email','password1')

    def validate(self,attrs):
        if attrs['password']!=attrs['password1']:
            raise serializers.ValidationError({'password':'password not match'})
        return attrs
    def create(self, validated_data):
        validated_data.pop('password1')
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            email=validated_data['email'],

        )    
        return user



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'
class BorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowRequest
        fields='__all__'
