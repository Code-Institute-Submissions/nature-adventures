from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.

REGIONS =  (
    ("Wales", "Wales"),
    ("Scotland", "Scotland"),
    ("N. Ireland", "Northern Ireland"),
    ("London", "London"),
    ("North East", "North East"),
    ("North West", "North West"),
    ("Yorks", "Yorkshire"),
    ("East Midlands", "East Midlands"),
    ("West Midlands", "West Midlands"),
    ("South East", "South East"),
    ("East of England", "East of England"),
    ("South West", "South West"),
)

#https://dev.to/earthcomfy/django-user-profile-3hik
#https://www.youtube.com/watch?v=KNvSWubOaQY
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(choices=REGIONS)
    profile_pic = CloudinaryField('image', default="placeholder")
    about = models.TextField()

    def __str__(self):
        return f"{self.user.username}"

#Create Profile automatically when new user signs up
#https://docs.djangoproject.com/en/5.1/topics/signals/
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)