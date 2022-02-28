from django.contrib import admin
from .models import HomeBanner
# Register your models here.

@admin.register(HomeBanner)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'BannerImage')