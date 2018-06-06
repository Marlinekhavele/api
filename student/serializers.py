from rest_framework import serializers
from .models import Student,Exam
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from .models import Student



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


class StudentSignupSerializer(serializers.ModelSerializer):
    """
    create a new student
    """
    class Meta:
        model = Student
        fields = (
            'user',
            'country',
            'county',
            'school',
            'phone_number'
        )

        # create the student
        def create(self,validated_data):
            new_created_student = Student(
                user = validated_data['user'],
                country = validated_data['country'],
                county = validated_data['county'],
                school = validated_data['school'],
                phone_number = validated_data['phone_number']
               
            )
            new_created_student.save()
            return new_created_student



















class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password"
            
        )

    def create(self, validated_data):
        user =User(
            username =validated_data["username"],
            first_name =validated_data["first_name"],
            last_name =validated_data["last_name"],
            
        )
        user.set_password(validated_data["password"])

        user.save()
        return user




class StudentCreateSerializer(serializers.ModelSerializer):
    """
    create a student from the cleaned data
    """
    class Meta:
        model = Student
        fields = (
            "user",
            "phone_number",
            "country",
            "county",
            "school"
        ) 
        def create(self,validated_data):
            new_student = Student(
                user=validated_data['user'],
                phone_number = validated_data["phone_number"],
                country = validated_data["country"],
                county =validated_data["county"],
                school= validated_data["school"]
            )
            new_student.save()
            return new_student
    # def create (self, validated_data):
    #      student =Student(
    #          user = validated_data["user"],
    #          phone_number = validated_data["phone_number"],
    #          country = validated_data["country"],
    #          county =validated_data["county"],
    #          school= validated_data["school"]
    #      )
    #      student.save()
    #      return student