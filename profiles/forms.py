from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['region', 'profile_pic', 'about']