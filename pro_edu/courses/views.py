from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course,Section,Video
from .serializers import CourseSerializer,SectionSerializer,VideoSerializer

# Create your views here.
class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.select_related().all()
    serializer_class = CourseSerializer

class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
