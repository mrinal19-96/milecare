

from django.contrib import admin
from .models import HomeBanner, HomeBoxSection, HomeProductivity, HomeInterface, HomeVideo, HomeTestimonial

# Register your models here.

@admin.register(HomeBanner)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','thumbnail_preview' )
    readonly_fields = ('thumbnail_preview',)
 
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    
# home box section
@admin.register(HomeBoxSection)
class HomeBoxAdmin(admin.ModelAdmin):
    list_display = ['id', 'BoxTitle', 'BoxDescription', 'BoxIcons', ]
    
# for home productivity section
@admin.register(HomeProductivity)
class HomeproductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'productivityImage_preview',
        'productivityHeading',
        'productivityDescription',
        'productivityTestimonial',
        'writterImage_preview',
        'writterBy',
        'productHeadingTwo',
        'productDescriptionTwo',
        'productTestimonialTwo',
        'ProductImageTwo_preview',
        'writter_by',
        'writterImageTwo_preview',
        
        ]
    # for banner Image
    readonly_fields = ('productivityImage_preview',)
    def productivityImage_preview(self, obj):
        return obj.productivityImage_preview

    productivityImage_preview.short_description = 'Productivity Preview'
    productivityImage_preview.allow_tags = True
    # for writer image
    readonly_fields = ('writterImage_preview',)
    def writterImage_preview(self, obj):
        return obj.writterImage_preview

    writterImage_preview.short_description = 'writter Preview'
    writterImage_preview.allow_tags = True
    
    # for seccond banner Image 
    readonly_fields = ('ProductImageTwo_preview',)
    def ProductImageTwo_preview(self, obj):
        return obj.ProductImageTwo_preview

    ProductImageTwo_preview.short_description = 'Productivity Two Preview'
    ProductImageTwo_preview.allow_tags = True
    
       # for seccond  writterImageTwo_preview 
    readonly_fields = ('writterImageTwo_preview',)
    def writterImageTwo_preview(self, obj):
        return obj.writterImageTwo_preview

    writterImageTwo_preview.short_description = 'writter Two Preview'
    writterImageTwo_preview.allow_tags = True
    
# for interface
@admin.register(HomeInterface)
class HomeinterfaceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'InterfaceHeading',
        'InterfaceDescription',
        'InterfaceBannerImage_preview',
        'titleOne',
        'headingOne',
        'titleTwo',
        'headingtwo',
        'TitleThree',
        'headingthree',
        'titleFour',
        'headingfour',
        
        ]
    
    # for seccond  InterfaceBannerImage 
    readonly_fields = ('InterfaceBannerImage_preview',)
    def InterfaceBannerImage_preview(self, obj):
        return obj.InterfaceBannerImage_preview

    InterfaceBannerImage_preview.short_description = 'Iterface banner Two Preview'
    InterfaceBannerImage_preview.allow_tags = True
    
# for video section
@admin.register(HomeVideo)
class HomeAdminVideo(admin.ModelAdmin):
    list_display = ['id','Heading', 'Description','video_link']
    
# for Testimonial section
@admin.register(HomeTestimonial)
class HomeAdminTestimonial(admin.ModelAdmin):
    list_display = ['id','content','writer_by']
    
      # for seccond  InterfaceBannerImage 
    # readonly_fields = ('writer_by_Image_preview',)
    # def writer_by_Image_preview(self, obj):
    #     return obj.writer_by_Image_preview

    # writer_by_Image_preview.short_description = 'writer Image Preview'
    # writer_by_Image_preview.allow_tags = True
    