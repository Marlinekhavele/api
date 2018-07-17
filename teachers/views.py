# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import permissions
from rest_framework.reverse import reverse

from .models import Teacher
from .serializers import (
    TeacherLoginSerializer,
    TeacherSignupSerializer,
    UserSignupSerializer,
    HeadTeacherSignupSerializer,
    CountyOfficerSignupSerializer,
    UserLoginSerializer

     )
# from .forms import (
#     Teacher_Signup
# )
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import(
    authenticate,
    login
   
)

# Create your views here.
# def  TeacherSignup(request):
#     """
#     This is a signup form
#     """
#     form = Student_Signup(request.POST or None)
#     context={'form':form}
#     template_name ='signup.html'

#     return render(request,template_name,context)

class UserRegisterAPIView(APIView):
    """
    user signup endpoint
    """

    def post(self,request,*args,**kwargs):


        username=request.data["username"]
        first_name=request.data["first_name"]
        last_name=request.data["last_name"]
        password=request.data["password"]
        


        data = {
                "username":username,
                "first_name":first_name,
                "last_name":last_name,
            }


        usercreate_serializer = UserSignupSerializer(data=data)
        if usercreate_serializer.is_valid():
            new_user = usercreate_serializer.save()
            # token = Token.objects.get(user=user)
    
            return Response(usercreate_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(usercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    # permission_classes([permissions.AllowAny,])
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self,request,*args,**kwargs):
        data =request.data
        serializer_class = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception =True):
            new_data = serializer.data
            return Response(new_data,status = HTTP_200_OK)
        return Response(serializer.errors,status =HTTP_400_BAD_REQUEST)

class TeacherRegisterAPIView(APIView):
    """
    user signup endpoint
    """

    def post(self,request,*args,**kwargs):

        user = request.data["user"]
        role = request.data["role"]
        county=request.data["county"]
        school=request.data["school"]
       

        data = {
                "user":user,
                "role":role,
                "county":county,
                "school":school,
               
            }


        teachercreate_serializer = TeacherSignupSerializer(data=data)
        if teachercreate_serializer.is_valid():
            new_teacher = teachercreate_serializer.save()
            token = Token.objects.get(user=user)
            
            return Response(teachercreate_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(teachercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TeacherLoginAPIView(APIView):
    """
     teacher login endpoint
    """
    def post(self,request,*args,**kwargs):
        user = request.data["user"]
        role = request.data["role"]
        county=request.data["county"]
        school=request.data["school"]


        data = {
                "user":user,
                "role":role,
                "county":county,
                "school":school,
        }


        

        teacherupdate_serializer =TeacherLoginSerializer(data=data)
        if teacherupdate_serializer.is_valid():
            teacher_update = teacherupdate_serializer.save()
            token = Token.objects.get(user=user)
            return Response(teacherupdate_serializer.data,status=status.HTTP_201_CREATED)
        return Response(teacherupdate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class HeadTeacherRegisterAPIView(APIView):
    """
    user signup endpoint
    """

    def post(self,request,*args,**kwargs):

        user = request.data["user"]
        role = request.data["role"]
        county=request.data["county"]
        school=request.data["school"]
       

        data = {
                "user":user,
                "role":role,
                "county":county,
                "school":school,
               
            }


        headteachercreate_serializer = HeadTeacherSignupSerializer(data=data)
        if headteachercreate_serializer.is_valid():
            new_headteacher = headteachercreate_serializer.save()
            token = Token.objects.get(user=user)
            
            return Response(headteachercreate_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(headteachercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CountyOfficerRegisterAPIView(APIView):
    """
    user signup endpoint
    """

    def post(self,request,*args,**kwargs):

        user = request.data["user"]
        role = request.data["role"]
        county=request.data["county"]
        school=request.data["school"]
       

        data = {
                "user":user,
                "role":role,
                "county":county,
                "school":school,
               
            }


        CountyOfficercreate_serializer = CountyOfficerSignupSerializer(data=data)
        if CountyOfficercreate_serializer.is_valid():
            new_CountyOfficer = CountyOfficercreate_serializer.save()

            
            token = Token.objects.get(user=user)
            
            return Response(CountyOfficercreate_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(CountyOfficercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


