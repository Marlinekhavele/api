# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.compat import authenticate
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.urls import login
from rest_framework.reverse import reverse

from .models import People
from .serializers import LoginSerializer
from .serializers import CreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.authtoken.models import Token


class APIRootView(APIView):
    def get(self, request, format=None):
        return Response({
            'login':reverse("login",request=request,format=format),
            'create':reverse("register",request=request,format=format),

        })
        # create =
        # data = {
            
        #     'createview-url': reverse('create-view', args=[create], request=request)
        #     'loginview-url': reverse('login-view', args=[login], request=request)
            
        # }
        # return Response(data)
        

class CreateView(APIView):
    """
    Description:\n A signup view\n
    Request type:\n POST \n
    Sample Post: \n{
        	"username":"laura",
	        "first_name":"laura",
	        "last_name":"pedro",
	        "email":"pedrola@gmail.com",
	        "password":"laura1999"
    }\n
    
    \nResponse success status:HTTP_201_created\n

    sample success:\n{
    "username": "laura",
    "token": "e06167b4a73d2eb3d9541586d88b546df217ffba",
    "email": "pedrola@gmail.com"
}\n

\nResponse Failure:\n{

 \nerror: bad request:	HTTP_400_BAD REQUEST\n

}\n
    """
    def post(self,request,*args,**kwargs):
        username=request.data["username"]
        first_name=request.data["first_name"]
        last_name=request.data["last_name"]
        email=request.data["email"]
        password=request.data["password"]


        data={
            "username":username,
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "password":password,

        }

        serializer_class=CreateSerializer(data=data)

        if serializer_class.is_valid():
            user =serializer_class.save()
            user.set_password(request.data["password"])
            user.save()
            token =  Token.objects.get(user=serializer_class.instance)
            success_response = {
                "user":user.id,
                "username":user.username,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email":user.email,
                "token":token.key
            }
            return Response(success_response,status=status.HTTP_201_CREATED)
            # return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def people_list(request):
#     """
#     List all people, or create a new people.
#     """
#     if request.method == 'GET':
#         people = People.objects.all()
#         serializer = PeopleSerializer(people, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PeopleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Description:\n A login view\n
    Request type:\n POST \n
    Sample Post: \n{
        	"username":"laura",
	        "password":"laura1999"
    }\n
    
    \nResponse success status:HTTP_200_OK\n

    sample success:\n{
    "username": "laura",
    "token": "e06167b4a73d2eb3d9541586d88b546df217ffba",
   
 }\n

 \nResponse Failure:\n{

 \nerror: Not found:	HTTP_404_NOT_FOUND\n

  }\n
"""
    
    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                print(user)
                print(user.id)
                 # login(request, user)
                token = Token.objects.get(user_id=user.id)
                print(token)

                success_user_response = {
                    "username":user.username,
                    "token":token.key

                 }
                return Response(success_user_response ,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)





    # def get(self, request, format=None):
    #     people = People.objects.all()
    #                      serializer = PeopleSerializer(people, many=True)
    #     return Response(serializer.data)


    #
    # def post(self, request, format=None):
    #     serializer = PeopleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


