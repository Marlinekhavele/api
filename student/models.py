# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User)
    phone_number = PhoneNumberField()
    country = models.CharField(max_length=50)
    county = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    def __str__(self):
        return self.country
    

# def __str__(self):
#     return self.country
#     # return str(self.Student)



class Exam(models.Model):
     name = models.CharField(max_length=130)
     subject = models.CharField(max_length=40)
     examtype = models.CharField(max_length=40)
     no_of_question = models.IntegerField()
     description = models.TextField()
     price =models.IntegerField()
     owner = models.CharField(max_length=60)




# def __str__(self):
#     return self.name
#     # return str(self.Exam)

