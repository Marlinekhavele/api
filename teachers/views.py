# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import permissions
from rest_framework.reverse import reverse

from .models import (
    Teacher,
    User
    )

from .serializers import (
    # TeacherLoginSerializer,
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

class APIRootView(APIView):
    """
    user endpoint is for user registration \n
    register is for teacher registration \n
    detail is for headteacher registration \n
    create is for countyofficer registration \n
    """
    def get(self, request, format=None):
        return Response({
            'user':reverse("user",request=request,format=format),
            'register':reverse("register",request=request,format=format),
            'detail':reverse("detail",request=request,format=format),
            'create':reverse("create",request=request,format=format),

        })

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
                "password":password
            }


        usercreate_serializer = UserSignupSerializer(data=data)
        if usercreate_serializer.is_valid():
            user = usercreate_serializer.save()
            user.set_password(password)
            user.save()
            print(user.id)
           
            # token = Token.objects.get(user=user)

            success_response = {
                "username":user.username,
                "first_name":first_name,
                "last_name":last_name,
                "token": token.key
                
            }
    
            return Response(success_response,status=status.HTTP_201_CREATED)
        
        return Response(usercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self,request,format=None):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(Q(username=username)).distinct()
        

        if user.exists() and user.count()  ==1:
            user_obj = user.first()
            
        else:
            error = {
                "error":"Sorry,This username is not valid!"
            }
            return Response(error,status=status.HTTP_403_FORBIDDEN)
        if user_obj:
            if not user_obj.check_password(password):
                error = {
                    "error":"Sorry This password is not valid!"
                }
                return Response(error,status=status.HTTP_403_FORBIDDEN)
            token = Token.objects.get(user_id=user_obj.id)
            login_response = {
                "key":token.key,
                "username":user_obj.username
            }
        return Response(login_response, status=status.HTTP_200_OK)


# class TeacherRegisterAPIView(APIView):
#     """
#     user signup endpoint
#     """

#     def post(self,request,*args,**kwargs):
        
        # username = request.user
        # if User.objects.filter(username=username).exists():
        #     user = User.objects.get(username=username)
        #     if User.objects.filter(username=request.data["username"]).exists()and user.username != request.data["username"]:
        # username = request.user
        # if User.objects.filter(username=username).exists():
        #     user = User.objects.get(username=username)
        #     if User.objects.filter(username=request.data["username"]).exists()and user.username != request.data["username"]:
        #         try:
        #             teacher = Teacher.objects.prefetch_related('user').get(user_id=user.id)
        #             try:
        #                 created = Result.objects.prefetch_related('teacher').filter(
        #               teacher_id=teacher.id
        #               ).values( "created")
        #                 response = {
        #                   "created":created
        #                   }
        #                 return Response(response, status=status.HTTP_200_OK)
        #         try:
        #             teacher = Teacher.objects.prefetch_related('user').get(user_id=user.id)
        #             try:
        #                 created = Result.objects.prefetch_related('teacher').filter(
        #               teacher_id=teacher.id
        #               ).values( "created")
        #                 response = {
        #                   "created":created
        #                   }
        #                 return Response(response, status=status.HTTP_200_OK)
                #         username=request.data["username"]
                #         first_name=request.data["first_name"]
                #         last_name=request.data["last_name"]
                #         password=request.data["password"]
                        
                #         data = {

                #         "user":user,
                #         "first_name":first_name,
                #         "last_name":last_name,
                #         "password":password
                #          }
                #         user = UserSignupSerializer(user,data=data)
                #         if user.is_valid():
                #             user = UserSignupSerializer.save()
                #             return Response(success, status.HTTP_201_CREATED)
                #         return Response(UserSignupSerializer.errors, status.HTTP_400_BAD_REQUEST)
                #         data ={
                #           "user": user.id,
                #           "role":request.data["role"],
                #           "county": request.data["county"],
                #           "school": request.data["school"]
                #        }
                #         teacher = teacher.objects.get(user_id=user.id)
                #         teacher = TeacherSignupSerializer(teacher, data=data)
                #         if teacher.is_valid():
                #            teacher.save()
                #            token = Token.objects.get(user_id=user.id)
                #            success_response = {
                #             'user_details': {
                #             "first_name": user.first_name,
                #             "last_name": user.last_name,
                #             "username": user.username,
                #             "token": token.key
                #             },
                #             "teacher_details":TeacherSignupSerializer.data
                #             }
                #             return Response(success_response, status=status.HTTP_201_CREATED)
                #         return Response(teachercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)       
                          
                #         return Response(serializer.data)
                #             return Response(teachercreate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # error ={
                #     "error":"user does not exit"
                # }
                # return Response(error,status.HTTP_400_BAD_REQUEST)
       
        


       

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
    HTTP 201 Created
   Allow: POST 

   { 
    "username":"sharon", 
    "first_name":"marline", 
    "last_name":"khavele",
    "password":"password",
    "is_headteacher":"true",
    "role":"headteacher",
    "county":1,
    "school":1 
    }


    {
    "username": "sharon",
    "school": 1,
    "county": 1,
    "token": "172d159b5c7a0b297c371583cf8c046f2c659e8e",
    "role": "headteacher",
    "user": 27
}
    """

    def post(self,request,*args,**kwargs):

        username=request.data["username"]
        first_name=request.data["first_name"]
        last_name=request.data["last_name"]
        password=request.data["password"]
        is_headteacher=request.data["is_headteacher"]
        role=request.data["role"]
        county=request.data["county"]
        school=request.data["school"]

        data = {
                "username":username,
                "first_name":first_name,
                "last_name":last_name,
                "password":password
               
            }

        usercreate_serializer = UserSignupSerializer(data=data)
        if usercreate_serializer.is_valid():
            user = usercreate_serializer.save()
            user.set_password(password)
            user.save()
             # define the data to be used by the headteacher serializer
            data = {

                "user":user.id,
                "is_headteacher":is_headteacher,
                "role":role,
                "county":county,
                "school":school
            }
            


        headteachercreate_serializer = HeadTeacherSignupSerializer(data=data)
        if headteachercreate_serializer.is_valid():
            new_headteacher = headteachercreate_serializer.save()
            token = Token.objects.get(user=user)

            success_headteacher_response ={
                        "user":user.id,
                        "username":user.username,
                        "role":role,
                        "county":county,
                        "school":school,
                        "token": token.key
                  
            }
            
            return Response(success_headteacher_response,status=status.HTTP_201_CREATED)
        return Response(headteachercreate_serializer.errors,status=HTTP_400_BAD_REQUEST)
        return Response(usercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
        


class CountyOfficerRegisterAPIView(APIView):
    """
    user signup endpoint \n
    { 
    "username":"shennaz", 
    "first_name":"marline", 
    "last_name":"khavele",
    "password":"password",
    "is_countyofficer":"true",
    "role":"countyofficer",
    "county":1,
    "school":1 
    }
    {
    "username": "maaaarina",
    "school": 1,
    "county": 1,
    "token": "dfd8d99c70170a9c7220c118082ea4456398fe03",
    "role": "countyofficer",
    "user": 26
}

     {
    "username": "marioghgsdjgjkshdcfdcjjnk",
    "county": 1,
    "school": 1,
    "role": "COUNTYOFFICER",
    "user": 21
    }
    {
    "username": "Annie",
    "county": 1,
    "school": 1,
    "role": "COUNTYOFFICER",
    "user": 22
}
\n I have changed the role not to take capital letters \n 
{
    "username": "wairimu",
    "county": 1,
    "school": 1,
    "role": "countyofficer",
    "user": 23
}
\n
    HTTP 201 Created
   Allow: POST
   

    """

    def post(self,request,*args,**kwargs):
        
        username=request.data["username"]
        first_name=request.data["first_name"]
        last_name=request.data["last_name"]
        password=request.data["password"]
        is_countyofficer=request.data["is_countyofficer"]
        role=request.data["role"]
        county=request.data["county"]
        school=request.data["school"]

        data = {
                "username":username,
                "first_name":first_name,
                "last_name":last_name,
                "password":password

               
                }

        usercreate_serializer = UserSignupSerializer(data=data)
        if usercreate_serializer.is_valid():
                user =usercreate_serializer.save()
                user.set_password(password)
                user.save()

                 # define the data to be used by the countyofficer serializer
                data ={

                "user":user.id,
                "is_countyofficer":is_countyofficer,
                "role":role,
                "county":county,
                "school":school

                 }

                countyofficercreate_serializer = CountyOfficerSignupSerializer(data =data)
                if countyofficercreate_serializer.is_valid():
                    new_countyofficer = countyofficercreate_serializer.save()
                    token = Token.objects.get(user=user)
                    
                    success_countyofficer_response = {
                        "user":user.id,
                        "username":user.username,
                        "role":role,
                        "county":county,
                        "school":school,
                        "token": token.key
                    }
                    return Response(success_countyofficer_response,status.HTTP_201_CREATED)
                return Response(countyofficercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(usercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            


        



class TeacherRegisterAPIView(APIView):
    """
    user signup endpoint \n
    { 
    "username":"marlinek", 
    "first_name":"marline", 
    "last_name":"khavele",
    "password":"password",
    "is_teacher":"true",
    "role":"teacher",
    "county":1,
    "school":1 
    }

    {
    "username": "peterG",
    "county": 1,
    "school": 1,
    "role": "teacher",
    "user": 12
}

{
    "username": "museic",
    "county": 1,
    "school": 1,
    "role": "TEACHER",
    "user": 17
}
HTTP 201 Created
Allow: POST
    """

    def post(self,request,*args,**kwargs):


        username=request.data["username"]
        first_name=request.data["first_name"]
        last_name=request.data["last_name"]
        password=request.data["password"]
        is_teacher = request.data["is_teacher"]
        role = request.data["role"]
        county=request.data["county"]
        school=request.data["school"]

        


        data = {
                "username":username,
                "first_name":first_name,
                "last_name":last_name,
                "password":password
            }


        usercreate_serializer = UserSignupSerializer(data=data)
        if usercreate_serializer.is_valid():
            user = usercreate_serializer.save()
            user.set_password(password)
            user.save()
            

            # define the data to be used by the teacher serializer
            data = {
                "user":user.id,
                "is_teacher":is_teacher,
                "role":role,
                "county":county,
                "school":school
            }


            teacher_create_serializer = TeacherSignupSerializer(data=data)
            
            if teacher_create_serializer.is_valid():
                new_teacher = teacher_create_serializer.save()
                token = Token.objects.get(user=user)

                success_teacher_response = {
                    "user":user.id,
                    "username":user.username,
                    "role":role,
                    "county":county,
                    "school":school,
                    "token": token.key
                }
                return Response(success_teacher_response,status=status.HTTP_201_CREATED)
            return Response(teacher_create_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        return Response(usercreate_serializer.errors,status=status.HTTP_400_BAD_REQUEST)