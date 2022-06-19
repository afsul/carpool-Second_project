
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    firstname=serializers.CharField(max_length=45)
    lastname=serializers.CharField(max_length=45)
    email=serializers.CharField(max_length=80)
    phone=serializers.IntegerField()
    date_of_birth=serializers.DateField()
    username=serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8,write_only=True)
   
    
   
    class Meta:
        model=User
        fields=['firstname','lastname','email','phone','date_of_birth','username','password','drivingliscenceno','drivfile']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)