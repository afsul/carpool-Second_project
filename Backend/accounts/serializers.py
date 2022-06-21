
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class SignUpSerializer(serializers.ModelSerializer):
   
    
   
    class Meta:
        model=User
        fields='__all__'

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):   
        password= validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        # ...
        return token