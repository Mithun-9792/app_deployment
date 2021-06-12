from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserProfileInfo(models.Model):

    #Create relationship (don't inherit from User!)
    user = models.BigAutoField(User,on_delete=models.CASCADE)

    #Add additional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
         
