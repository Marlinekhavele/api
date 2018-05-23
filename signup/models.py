# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models 
 # from django.contrib.auth import get_user_model
 # User = get_user_model()



from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class People(models.Model):
    # User._meta.get_field('username')._unique = True
    user = models.ForeignKey(User)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)


def __str__(self):
    return str(self.people)




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

