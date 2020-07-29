from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField()

class category(models.Model):
    cname = models.CharField(max_length=100)
    cimage = models.ImageField()

class subcategory(models.Model):
    scname = models.CharField(max_length=100)
    scimage = models.ImageField()
    cid = models.ForeignKey(category, on_delete=models.CASCADE)

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']