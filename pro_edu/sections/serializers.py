from rest_framework import serializers
from .models import Header,Footer,About,Teaching,ContactUs,SocialLinks,Logo,Mobile


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ['url','description','icon']



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['email','whatsapp','telegram','phone','land_line_phone','location']


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['image']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['description']


class TeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaching
        fields = ['join_us']






class HeaderSerializer(serializers.ModelSerializer):
    logo = LogoSerializer()

    class Meta:
        model = Header
        fields = ['logo']

    def create(self, validated_data):
        logo = validated_data['logo']
        validated_data['logo'] = Logo.objects.create(**logo)
        header =  super(HeaderSerializer,self).create(validated_data)

        return header






    def update(self, instance, validated_data):
        logo = validated_data['logo']
        header = Header.objects.filter(id=validated_data['id'])
        instance = super(FooterSerializer, self).update(instance, validated_data)
        return instance








class FooterSerializer(serializers.ModelSerializer):
    social_links = SocialLinksSerializer(many=True)
    logo = LogoSerializer()
    contact_us = ContactUsSerializer()
    teaching = TeachingSerializer()
    about = AboutSerializer()
    class Meta:
        model = Footer
        fields = ['contact_us','about','teaching','logo','social_links','id']

    def create(self, instance, validated_data):
        footer = Footer.objects.get(id=validated_data['id'])
        contact_us = validated_data['contact_us']
        about = validated_data['about']
        teaching = validated_data['teaching']
        logo = validated_data['logo']
        social_links = validated_data['social_links']
        validated_data['contact_us'] = ContactUs.objects.create(**contact_us)
        validated_data['logo'] = Logo.objects.create(**logo)
        footer = super(FooterSerializer,self).create(validated_data)
        for social_link in social_links:
            SocialLinks.objects.create(
                **social_link,
            )

        return footer

    def update(self, instance,validated_data):
        social_links = validated_data['social_links']
        contact_us = validated_data['contact_us']
        about = validated_data['about']
        teaching = validated_data['teaching']
        instance = super(FooterSerializer, self).update(instance, validated_data)
        logo = validated_data['logo']
        try:
            contact_us_object = ContactUs.objects.filter(id=contact_us['id']).first()
            validated_data['contact_us'] = ContactUs.objects.filter(pk=contact_us_object.pk).update()
        except:
            validated_data['contact_us'] = ContactUs.objects.create(**contact_us)

        for social_link in social_links:
            try:
                social_link_obj = SocialLinks.objects.filter(id=social_link['id']).first()
                image = social_link.pop('icon', None)
                social_link_obj.icon = image
                social_link_obj.save()
                SocialLinks.objects.filter(pk=social_link_obj.pk).update(**social_link)
            except:
                SocialLinks.objects.create(**social_link, footer=instance, )

        return instance





