from django.db import models
from moviepy.editor import VideoFileClip


# Create your models here.

class Courses(models.Model):
    description = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=30)
    number_of_enrollment = models.IntegerField()



class Sections(models.Model):
    number = models.PositiveIntegerField()
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    duration = models.CharField(max_length=30)

class Videos(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='')
    subtitles = models.FileField(upload_to='')
    section = models.ForeignKey(Sections,on_delete=models.CASCADE)
    duration = models.CharField(max_length=30)


    def get_duration(self):
        clip = VideoFileClip(self.content)
        duration = clip.duration
        minutes = int(duration/60)
        seconds = int(duration%60)
        result = str(minutes) + ':' + str(seconds)
        return result





