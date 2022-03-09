# Generated by Django 4.0.1 on 2022-03-09 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
     
     
      
     
       
        migrations.CreateModel(
            name='HomeInterface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InterfaceHeading', models.CharField(max_length=255)),
                ('InterfaceDescription', models.TimeField()),
                ('InterfaceBannerImage', models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/')),
                ('titleOne', models.CharField(max_length=255)),
                ('headingOne', models.CharField(max_length=255)),
                ('titleTwo', models.CharField(max_length=255)),
                ('headingtwo', models.CharField(max_length=255)),
                ('TitleThree', models.CharField(max_length=255)),
                ('headingthree', models.CharField(max_length=255)),
                ('titleFour', models.CharField(max_length=255)),
                ('headingfour', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]