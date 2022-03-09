from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class HomeBanner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    
# for image field
    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.thumbnail.url))
        return ""
    
# Home box
class HomeBoxSection(models.Model):
    BoxTitle = models.CharField(max_length=255)
    BoxDescription = models.TextField()
    BoxIcons = models.CharField(max_length=255)
    
# Home productivity section  
class HomeProductivity(models.Model):
    productivityImage = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    productivityHeading = models.CharField(max_length=255)
    productivityDescription = models.TextField()
    productivityTestimonial = models.CharField(max_length=255)
    writterImage = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    writterBy = models.CharField(max_length=255)
    productHeadingTwo = models.CharField(max_length=255, null=True)
    productDescriptionTwo = models.TextField(null=True)
    productTestimonialTwo = models.CharField(max_length=255 , null=True)
    ProductImageTwo = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    writter_by = models.CharField(max_length=255, null=True)
    writterImageTwo = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    # for image field productivityImage_preview
    @property
    def productivityImage_preview(self):
        if self.productivityImage:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.productivityImage.url))
        return ""
    
      # for image writterImage_preview
    @property
    def writterImage_preview(self):
        if self.writterImage:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.writterImage.url))
        return ""
    
    # for ProductImageTwo
    @property
    def ProductImageTwo_preview(self):
        if self.ProductImageTwo:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.ProductImageTwo.url))
        return ""
    
    # for writterImageTwo
    @property
    def writterImageTwo_preview(self):
        if self.writterImageTwo:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.writterImageTwo.url))
        return ""
    
    
# for Interface 
class HomeInterface(models.Model):
    InterfaceHeading = models.CharField(max_length=255)
    InterfaceDescription = models.TextField()
    InterfaceBannerImage = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    titleOne = models.CharField(max_length=255)
    headingOne = models.CharField(max_length=255)
    titleTwo = models.CharField(max_length=255)
    headingtwo = models.CharField(max_length=255)
    TitleThree = models.CharField(max_length=255)
    headingthree = models.CharField(max_length=255)
    titleFour = models.CharField(max_length=255)
    headingfour = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, default="", on_delete=models.CASCADE, null=True)
    
    # for writterImageTwo
    @property
    def InterfaceBannerImage_preview(self):
        if self.InterfaceBannerImage:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.InterfaceBannerImage.url))
        return ""
    
   
 