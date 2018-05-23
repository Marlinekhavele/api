from rest_framework import serializers
from .models import People
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



#
# class PeopleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = People
#         fields = ('id', 'user', 'password', 'phone_number', 'email')
#


class LoginSerializer(serializers.ModelSerializer):
    """
    ``Serializer`` for ``User`` ..
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name' , 'password', 'is_active', 'is_staff')
        read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
        #     'security_question': {'write_only': True},
        #     'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        """
        Update and return an existing `user` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance


def create(self, validated_data):
        """
        Create and return a new `user` instance, given the validated data.
        """
        return User.objects.create(**validated_data)




class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password",
            "email"
        )

    def create(self, validated_data):
        user =User(
            username =validated_data["username"],
            first_name =validated_data["first_name"],
            last_name =validated_data["last_name"],
            email =validated_data["email"]
        )
        user.set_password(validated_data["password"])

        user.save()
        return user
