

from django.contrib import admin
from .models import HomeBanner, HomeBoxSection

# Register your models here.

@admin.register(HomeBanner)

class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','thumbnail_preview' )
    readonly_fields = ('thumbnail_preview',)
 
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
@admin.register(HomeBoxSection)
class HomeBoxAdmin(admin.ModelAdmin):
    list_display = ['id', 'BoxTitle', 'BoxDescription', 'BoxIcons', ]