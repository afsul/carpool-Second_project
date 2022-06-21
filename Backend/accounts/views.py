

from .serializers import MyTokenObtainPairSerializer, SignUpSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView




class SignupView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def post(self,request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response={
                "message":"User Created Successfully",
                "data":serializer.data
            }

            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(email,"<--------------This is email-------------->")
        print(password,"<--------------This is password-------------->")
        user = authenticate(email=email, password=password)
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            if check_password(password,user.password):
                  
                print(user,"<--------------This is user-------------->")
                response = {"message": "Login Successfull", "token": user.auth_token.key}
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                return Response(data={"message": "Invalid email or password,,,,,,"})
        # if user is not None:
            

        #     # tokens = create_jwt_pair_for_user(user)

        #     response = {"message": "Login Successfull", "token": user.auth_token.key}
        #     return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password///////////"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)

class Mytoken_view(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

