from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from django import forms
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    profile_pic = CloudinaryFileField()

    class Meta:
        model = Profile
        fields = ['region', 'profile_pic', 'about']