from django import forms
from .models import Hike


class CreateHikeForm(forms.ModelForm):
    """
    Form class for users to create a new hike
    """
    class Meta:
        """
        Specifies the model and fields displayed
        """
        model = Hike
        fields = [
            'hike_name',
            'region',
            'distance',
            'description',
            'route_image'
        ]
