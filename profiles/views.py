from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Profile

# Create your views here.

@login_required
def profile(request, username):
    # Get the username of the current user
    users = User.objects.all()
    username = get_object_or_404(users, username=request.user.username)
    # Get the profile of the current user using the username
    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, user=username)
    return render(
            request, 
            "profiles/profile.html", 
            {"profile":profile}
            )