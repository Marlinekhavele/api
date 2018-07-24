from rest_framework import serializers
from .models import Teacher
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.serializers import(
    CharField,
    EmailField,
    ValidationError,
    ModelSerializer,
    SerializerMethodField,

)
from .models import (
    Teacher,
    HeadTeacher,
    CountyOfficer,
    TEACHER_CHOICES
    )



class UserSignupSerializer(serializers.ModelSerializer):
    """
    serializer responsible during a user registration
    """
    class Meta:
        model = User
        fields = (
            'username',
            'last_name',
            'last_name',
            'password',
        )
        write_only_fields = ('password',)
        read_only_fields=('is_staff','is_superuser','is_active')

        def create(self,validated_data):
            user = User(
                username = validated_data['username'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],

            )
            
            user.set_password(validated_data['password'])
            user.save()
            return user

class UserLoginSerializer(ModelSerializer):
    username = CharField(required = False, allow_blank = True)
    email = EmailField(label ='Email Address',required = False, allow_blank = True)
    class Meta:
        model = User
        fields ={
            'username',
            'password',
            'token'
        }
        extra_kwargs ={'password':
        {"write_only":True}
        }
        def validate (self,data):
            user_obj = None
            # email = data.get["email",None]
            username = data.get["username",None]
            password = data["password"]
            if  not username:
                raise ValidationError("username or email is required")

                user = user.objects.filter(
                    # Q(email = email),
                    Q(username = username)
                ).distinct()
                user = user.exclude(email_isnull =True).exclude(email_iexact ='')
                if user.exists()and user.count()==1:
                    user = user.first()
                else:
                        raise ValidationError("This username/email is not valid")
                        if user_obj:
                            if not user_obj.check_password:
                                raise ValidationError("Incorrect username and password try again")
                                data[token]
                                return data

class TeacherSignupSerializer(serializers.ModelSerializer):
    """
    serializer responsible during a teacher registration
    """
    TEACHER_CHOICES = ("teacher","headteacher","countyofficer")

    role = serializers.ChoiceField(choices=TEACHER_CHOICES)
    class Meta:
        model = Teacher
        fields = (
            'user',
            'is_teacher',
            'role',
            'county',
            'school'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        )
        write_only_fields = ('password',)
        read_only_fields=('is_staff','is_superuser','is_active','is_teacher')
       
        def create(self,validated_data):
            new_created_teacher = Teacher(
                user=validated_data['user'],
                is_teacher = validated_data['is_teacher'],
                role = validated_data['role'],
                county = validated_data['county'],
                school = validated_data['school']

            )
            
            # new_created_teacher.set_password(validated_data['password'])
            new_created_teacher.save()
            return new_created_teacher





class HeadTeacherSignupSerializer(serializers.ModelSerializer):
    """
    serializer responsible during a Headteacher registration
    """
    TEACHER_CHOICES = ("teacher","headteacher","countyofficer")

    role = serializers.ChoiceField(choices=TEACHER_CHOICES)


    class Meta:
        model = HeadTeacher
        fields = (
            'user',
            'is_headteacher',
            'role',
            'county',
            'school'
            
            

        )
        write_only_fields = ('password',)
        read_only_fields=('is_staff','is_superuser','is_active','is_headteacher')
       
        def create(self,validated_data):
            new_created_headteacher = HeadTeacher(
                user=validated_data['user'],
                is_headteacher = validated_data['is_headteacher'],
                role = validated_data['role'],
                county = validated_data['county'],
                school = validated_data['school']

            )
            
            new_created_headteacher.set_password(validated_data['password'])
            new_created_headteacher.save()
            return new_created_headteacher

class CountyOfficerSignupSerializer(serializers.ModelSerializer):
    """
    serializer responsible during a Headteacher registration

   
    """
    TEACHER_CHOICES = ("teacher","headteacher","countyofficer")
    role = serializers.ChoiceField(choices=TEACHER_CHOICES)
    class Meta:
        model = CountyOfficer
        fields = (
            'user',
            'is_countyofficer',
            'role',
            'county',
            'school'
            
            

        )
        write_only_fields = ('password',)
        read_only_fields=('is_staff','is_superuser','is_active')
       
        def create(self,validated_data):
            new_created_CountyOfficer = CountyOfficer(
                user=validated_data['user'],
                is_CountyOfficer = validated_data['is_CountyOfficer'],
                role = validated_data['role'],
                county = validated_data['county'],
                school = validated_data['school']

            )
            
            new_created_CountyOfficer.set_password(validated_data['password'])
            new_created_CountyOfficer.save()
            return new_created_CountyOfficer