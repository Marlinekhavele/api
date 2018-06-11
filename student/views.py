# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.reverse import reverse

from .models import Student,Exam
from .serializers import (
    CreateUserSerializer,
    StudentCreateSerializer,
    UserSignupSerializer,
    StudentSignupSerializer
    

     )
from .forms import UserLoginForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView





def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form =  UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        
    return render(request,"form.html",{"form":form})

class UserRegisterAPIView(APIView):
    """
    user signup endpoint
    """
    # def post(self,request,*args,**kwargs):
        # username=request.data["username"]
        # first_name=request.data["first_name"]
        # last_name=request.data["last_name"]
        # password=request.data["password"]
        # user = request.data["user"]
        # country=request.data["country"]
        # county=request.data["county"]
        # school=request.data["school"]
        # phone_number=request.data["phone_number"]


        # data = {
        #         "user":user,
        #         "country":country,
        #         "county":county,
        #         "school":school,
        #         "phone_number":phone_number,
        #     }


        # studentcreate_serializer = StudentSignupSerializer(data=data)
        # if studentcreate_serializer.is_valid():
        #     new_student = studentcreate_serializer.save()
        #     token = Token.objects.get(user=user)
        #     print(token.key)
        #     return Response(studentcreate_serializer.data,status=status.HTTP_201_CREATED)
        
        # return Response(studentcreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



        #     studentcreate_serializer = StudentSignupSerializer(data=data)

        #     if studentcreate_serializer.is_valid():
        #         new_student = studentcreate_serializer.save()
        #         token = Token.objects.get(user=usercreate_serializer.instance)


        #         success_user_response = {
        #             "user":user.id,
        #             "token":token.key
        #         }
        #         return Response(success_user_response,status=status.HTTP_201_CREATED)
        # return Response(usercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)




    def post(self,request,*args,**kwargs):


        # username=request.data["username"]
        # first_name=request.data["first_name"]
        # last_name=request.data["last_name"]
        # password=request.data["password"]
        user = request.data["user"]
        country=request.data["country"]
        county=request.data["county"]
        school=request.data["school"]
        phone_number=request.data["phone_number"]


        data = {
                "user":user,
                "country":country,
                "county":county,
                "school":school,
                "phone_number":phone_number,
            }


        studentcreate_serializer = StudentSignupSerializer(data=data)
        if studentcreate_serializer.is_valid():
            new_student = studentcreate_serializer.save()
            token = Token.objects.get(user=user)
            print(token.key)
            return Response(studentcreate_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(studentcreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)









# Create your views here.
class CreateView(APIView):

    def post(self,request,*args,**kwargs):
        username=request.data["username"],
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        password=request.data["password"],
        country=request.data["country"],
        county=request.data["county"],
        school=request.data["school"],
        phone_number=request.data["phone_number"]


        data={
            "username":username,
            "first_name":first_name,
            "last_name":last_name,
            "password":password,

        }

        serializer_class=CreateUserSerializer(data=data)

        if serializer_class.is_valid():
            user =serializer_class.save()
            user.set_password(request.data["password"])
            user.save()
            

            data = {
                "user":user.id,
                "country":country,
                "county":county,
                "school":school,
                "phone_number":phone_number,
            }

            student_serializer = StudentCreateSerializer(data=data)
            if student_serializer.is_valid():
                created_student = student_serializer.save()
                token =  Token.objects.get(user=serializer_class.instance)

                success_user_response = {
                    "user":user.id,
                    "username":user.username,
                    "first_name":user.first_name,
                    "last_name":user.last_name,

                }
                return Response(success_user_response,status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)