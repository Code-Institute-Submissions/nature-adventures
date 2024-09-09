from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.

REGIONS = (
    ("Wales", "Wales"),
    ("Scotland", "Scotland"),
    ("Northern Ireland", "Northern Ireland"),
    ("London", "London"),
    ("North East", "North East"),
    ("North West", "North West"),
    ("Yorkshire", "Yorkshire"),
    ("East Midlands", "East Midlands"),
    ("West Midlands", "West Midlands"),
    ("South East", "South East"),
    ("East of England", "East of England"),
    ("South West", "South West"),
)


class Profile(models.Model):
    """
    Stores a single profile related to :model:`auth.User`
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(choices=REGIONS, max_length=100)
    profile_pic = CloudinaryField('image', default="placeholder")
    about = models.TextField()

    def __str__(self):
        return f"{self.user.username}"


def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile automatically when a new user signs up
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
