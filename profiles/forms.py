from django import forms
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """
    Form class for users to update their profile
    """

    class Meta:
        """
        Specify django model and the fields
        """
        model = Profile
        fields = ['region', 'profile_pic', 'about']
