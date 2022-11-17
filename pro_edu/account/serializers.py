# from django.contrib.auth import password_validation
# from django.conf import settings
# from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from .models import User
# from phonenumber_field.serializerfields import PhoneNumberField
from djoser.serializers import UserCreateSerializer




class RegisterSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id','username','password','first_name','middle_name','last_name','phone','birth_date','gender']

