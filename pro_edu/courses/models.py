from django.db import models
from django_extensions.db.models import TimeStampedModel
from moviepy.editor import VideoFileClip
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


# Create your models here.


class Course(TimeStampedModel):
    description = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    number_of_enrollments = models.IntegerField()
    image = models.ImageField(upload_to="")
    rate = models.DecimalField(max_digits=2, decimal_places=1)

    def get_course_duration(self):
        for section in Course.sections.all():
            duration = section.duration
            hours = duration / 3600
            minutes = (duration % 3600) / 60
            seconds = duration % 60
            return {"hours": hours, "minutes": minutes, "seconds": seconds}

    def add_section_duration(self, duration):
        hours = duration.get("hours")
        minutes = duration.get("minutes")
        seconds = duration.get("seconds")
        return {"hours": hours, "minutes": minutes, "seconds": seconds}


class Section(TimeStampedModel):

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="sections"
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    duration = models.BigIntegerField()

    def add_video_duration(self, duration):
        hours = duration.get("hours")
        minutes = duration.get("minutes")
        seconds = duration.get("seconds")

        self.duration += seconds + (minutes * 60) + (hours * 3600)

    def get_section_duration(self):
        for video in Section.videos.all():
            duration = video.duration
            hours = duration / 3600
            minutes = (duration % 3600) / 60
            seconds = duration % 60
            return {"hours": hours, "minutes": minutes, "seconds": seconds}

    def __str__(self):
        return str(self.id) + ": " + self.title


class Video(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to="")
    subtitle = models.FileField(upload_to="")
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="videos"
    )
    duration = models.IntegerField()

    def get_video_duration(self):
        clip = VideoFileClip(self.content)
        duration = round(clip.duration)
        hours = duration / 3600
        minutes = (duration % 3600) / 60
        seconds = duration % 60
        return {"hours": hours, "minutes": minutes, "seconds": seconds}

    def find_between(s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""

    def validate_duration(self):
        temp = self.duration.replace(":", "")
        if (not temp.isnumeric()) or (self.duration.count(":") != 2):
            raise ValidationError(
                _("%(duration)d is not a number"), params={"duration": self.duration}
            )


class Enrollments(models.Model):
    customer = models.OneToOneField("account.Customer", on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_of_enrollment = models.DateTimeField(auto_now_add=True)
