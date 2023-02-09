from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')
    twitter = models.CharField(max_length=200,null=True,blank=True)
    slug = AutoSlugField(unique_with=['user__first_name','user__last_name'],)

