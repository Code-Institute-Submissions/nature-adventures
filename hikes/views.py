from django.shortcuts import render
from django.views import generic
from .models import Hike

# Create your views here.

class HikesList(generic.ListView):
    queryset = Hike.objects.all()
    template_name = "hikes/hikes_list.html"