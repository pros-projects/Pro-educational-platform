from rest_framework import serializers
from .models import Section,Video,Course

class VideoSerializer(serializers.ModelSerializer):
    section = serializers.HyperlinkedRelatedField(queryset= Section.objects.select_related('section').all(),view_name='')
    class Meta:
        model = Video
        fields = ['title','id','content','section','duration','subtitle']

class SectionSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    course = serializers.HyperlinkedRelatedField(queryset= Course.objects.select_related('course').all(),view_name='')
    class Meta:
        model = Section
        fields = ['course','title','description','duration','videos']

class CourseSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    class Meta:
        model = Course
        fields = ['title','description','duration','number_of_enrollments','sections','image','rate']

