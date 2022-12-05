from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel



# Create your models here.

# class Footer(models.Model):
class Logo(models.Model):
    image = models.ImageField()

class SocialLinks(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=255)
    icon = models.ImageField()

class About(models.Model):
    description = models.CharField(max_length=800)

class ContactUs(models.Model):
    email = models.EmailField()
    whatsapp = PhoneNumberField(region='SY',max_length=13)
    telegram = PhoneNumberField(region='SY',max_length=13)
    phone = PhoneNumberField(region='SY',max_length=13)
    land_line_phone = PhoneNumberField(region='SY',max_length=7)
    location = models.CharField(max_length=255)


class Teaching(models.Model):
    join_us = models.URLField()

class Mobile(models.Model):
    download_From = models.URLField()


class Footer(SingletonModel):
    contact_us = models.OneToOneField(ContactUs,on_delete=models.CASCADE)
    about = models.OneToOneField(About,on_delete=models.CASCADE)
    teaching = models.OneToOneField(Teaching,on_delete=models.CASCADE)
    logo = models.ForeignKey(Logo,on_delete=models.PROTECT)
    social_links = models.ForeignKey(SocialLinks,on_delete=models.PROTECT)
    def __str__(self):
        return f"that's a footer implemented using a singelton model and ID is {self.id}"


class Header(SingletonModel):
    logo = models.ForeignKey(Logo, on_delete=models.PROTECT)
    def __str__(self):  
        return f"that's a footer implemented using a singelton model and ID is {self.id}"

