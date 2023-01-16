from rest_framework import serializers
from .models import Section,Video,Course

class VideoSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True)
    class Meta:
        model = Video
        fields = ['title','id','content','section','duration','subtitle','course',]
    def validate(self, attrs):
        section = attrs.get('section')
        course = attrs["course"]
        if not course.sections.filter(pk=section.pk).exists():
            raise serializers.ValidationError("Section must be in the selected course")
        return attrs
    def create(self, validated_data):
        course = validated_data.pop('course',None)
        video = super(VideoSerializer,self).create(validated_data)
        return video



class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title','content','section','subtitle','course']

class SectionSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    class Meta:
        model = Section
        fields = ['course','title','description','duration','videos']
        read_only_fields = ['videos']
    def create(self, validated_data):
        videos = validated_data.pop("videos",[])
        section = super(SectionSerializer,self).create(validated_data)

        for video in videos:
            Video.objects.create(**video,section=section)
            duration = video.get_video_duration()
            section.add_video_duration(duration)
        section.save()
        return section

    def update(self, instance, validated_data):
        videos = validated_data.pop('videos',[])
        instance = super(SectionSerializer,self).update(instance,validated_data)
        for video in videos:
            try:
                video_obj = Video.objects.filter(id=video.id).first()
                video_obj.title = video.pop('title',None)
                video_obj.duration = video.get_video_duration()
                video_obj.subtitle = video.pop('subtitle',None)
                video_obj.content = video.pop('content',None)
                video_obj.save()
                instance.add_video_duration(video_obj.duration)
                Video.objects.filter(pk=video_obj.pk).update(**video)
            except:
                Video.objects.create(**video)
                instance.add_video_duration(video.pop('duration',None))
        instance.save()

        return instance





class CourseSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    class Meta:
        model = Course
        fields = ['title','description','duration','number_of_enrollments','sections','image','rate']
        read_only_fields = ['sections']

    def create(self, validated_data):
        sections = validated_data.pop("sections",[])
        course = super(CourseSerializer,self).create(validated_data)
        for section in sections:
            Section.objects.create(**section,course=course)
            duration = section.get_section_duration()
            course.add_section_duration(duration)
        course.save()

        return course


    def update(self, instance, validated_data):
        sections = validated_data.pop('sections',[])
        instance = super(CourseSerializer,self).update(instance,validated_data)
        for section in sections:
            try:
                section_obj = Section.objects.filter(id=section.id).first()
                section_obj.title = section.pop('title',None)
                section_obj.duration = section.get_section_duration()
                section_obj.description = section.pop('description','')
                videos = section.pop('videos',[])
                for video in videos:
                    try:
                        video_obj = Video.objects.filter(id=video.id).first()
                        video_obj.title = video.pop('title', None)
                        video_obj.duration = video.get_video_duration()
                        video_obj.subtitle = video.pop('subtitle', None)
                        video_obj.content = video.pop('content', None)
                        video_obj.save()
                        section.add_video_duration(video_obj.duration)
                        Video.objects.filter(pk=video_obj.pk).update(**video)
                    except:
                        Video.objects.create(**video)
                        section.add_video_duration(video.pop('duration',None))
                instance.add_section_duration(section_obj.duration)
                Section.objects.filter(pk=section_obj.pk).update(**section)
            except:
                Section.objects.create(**section)
                Course.add_section_duration(section.pop('duration',None))
        instance.save()
        return instance

