# Generated by Django 4.1.3 on 2022-11-24 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialLinkModel',
            new_name='SocialLinks',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='social_link',
            new_name='social_links',
        ),
    ]