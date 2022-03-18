from django.contrib import admin
from .models import NavMenu
# Register your models here.

@admin.register(NavMenu)
class NavAdminMenu(admin.ModelAdmin):
    lis_display = ['id']
