# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


TEACHER_CHOICES = (
    ("TEACHER", "teacher"),
    ("HEADTEACHER", "headteacher"),
    ("COUNTYOFFICER", "countyofficer")
    
)

class Country(models.Model):
    name =models.CharField(max_length=60) 
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)



class County(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(Country)
    def __str__(self):
        return str (self.name)



class School(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.country)



class Teacher(models.Model):
    user =models.OneToOneField(User) 
    is_teacher = models.BooleanField('teacher status', default=True)
    role = models.CharField(max_length=60,choices=TEACHER_CHOICES)
    school = models.ForeignKey(School, null=True, blank=True)
    county = models.ForeignKey(County, null=True, blank=True)
    def __str__(self):
        # return self.user
        return str(self.user)



class HeadTeacher(models.Model):
    user = models.OneToOneField(User)
    is_headteacher = models.BooleanField('headteacher status', default=True)
    role = models.CharField(max_length=60,choices=TEACHER_CHOICES)
    county = models.ForeignKey(County, null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True)
    def __str__(self):
      return str (self.user)

class CountyOfficer(models.Model):
    user = models.OneToOneField(User)
    is_countyofficer = models.BooleanField('countyofficer status', default=True)
    role = models.CharField(max_length=60,choices=TEACHER_CHOICES)
    county = models.ForeignKey(County, null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True)
    def __str__(self):
      return str(self.user)









   


    
