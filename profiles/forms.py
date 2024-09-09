from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """
    Form class for users to update their profile
    """
    profile_pic = CloudinaryFileField()

    class Meta:
        """
        Specify django model and the fields
        """
        model = Profile
        fields = ['region', 'profile_pic', 'about']
