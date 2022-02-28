from django.db import models

# Create your models here.
class HomeBanner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    BannerImage = models.ImageField(upload_to ='uploads/') 
    
