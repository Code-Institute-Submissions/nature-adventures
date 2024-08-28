from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

REGIONS =  (
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

class Hike(models.Model):
    hike_name = models.CharField(max_length=100, unique=True)
    region = models.CharField(choices=REGIONS)
    distance = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(200)
    ])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hiking_routes")
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    route_image = CloudinaryField('image', default='placeholder')

    class Meta: 
        pass

    def __str__(self):
        return f"{self.hike_name}"


