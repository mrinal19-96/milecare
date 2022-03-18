
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NavMenu(models.Model):
    MenuTitle = models.CharField(max_length=255)
    parent_id = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=255)
    level = models.IntegerField()
    MenuUrlName = models.CharField(max_length=255)
    subCategoryname = models.CharField(max_length=255)
    subCategoryUrlName = models.CharField(max_length=255)
    