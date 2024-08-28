from django import forms
from .models import Hike


class CreateHikeForm(forms.ModelForm):

    class Meta:
        model = Hike
        fields = ['hike_name', 'region', 'distance', 'description', 'route_image']
