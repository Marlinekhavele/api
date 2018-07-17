# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Country,County,School,Teacher, HeadTeacher,CountyOfficer

admin.site.register(Country)

admin.site.register(County)

admin.site.register(School)

admin.site.register(Teacher)

admin.site.register(HeadTeacher)

admin.site.register(CountyOfficer)
