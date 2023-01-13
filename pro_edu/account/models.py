from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.modelfields import PhoneNumberField

from django.conf import settings


class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    CHOICES = [(MALE, 'Male'), (FEMALE, 'Female')]
    middle_name = models.CharField(max_length=25)
    birth_date = models.DateField(null=True)
    gender = models.CharField(choices=CHOICES, default=MALE,max_length=25)
    username = models.CharField(max_length=25,unique=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = PhoneNumberField(region='SY',max_length=13)
    objects = CustomUserManager()



    def __str__(self):
        return self.first_name+" "+self.last_name+" AKA"+self.username


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    enrolled_at = models.ManyToManyField('courses.Course')
    tutor = models.BooleanField(default=False)




    def __str__(self):
        return f'customer {self.user.first_name} {self.user.last_name} with username {self.user.username} is enrolled'
    @property
    def is_tutor(self):
        if self.active and self.tutor:
            return True
        return False