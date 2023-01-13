from django.db import models
from django_extensions.db.models import TimeStampedModel
from moviepy.editor import VideoFileClip
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _



# Create your models here.

class Course(TimeStampedModel):
    description = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    number_of_enrollments = models.IntegerField()
    image = models.ImageField(upload_to='')
    rate = models.DecimalField(max_digits=2,decimal_places=1)





class Section(TimeStampedModel):

    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    duration = models.CharField(max_length=10)

class Video(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='')
    subtitle = models.FileField(upload_to='')
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    duration = models.CharField(max_length=6)


    def get_duration(self):
        clip = VideoFileClip(self.content)
        duration = clip.duration
        minutes = int(duration/60)
        seconds = int(duration%60)
        result = str(minutes) + ':' + str(seconds)
        return result

    def find_between(s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""
    def validate_duration(self):
        temp = self.duration.replace(':','')
        if (not temp.isnumeric() )or (self.duration.count(':') != 2):
            raise ValidationError(_('%(duration)d is not a number' ),params={'duration':self.duration})



class Enrollments(models.Model):
    customer = models.OneToOneField('account.Customer',on_delete=models.PROTECT)
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    date_of_enrollment = models.DateField(auto_now_add= True)


