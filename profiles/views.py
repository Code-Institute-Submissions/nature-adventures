from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Profile
from .forms import UpdateProfileForm

# Create your views here.

@login_required
def profile(request, username):
    # Get the username of the user
    users = User.objects.all()
    username = get_object_or_404(users, username=username)
    # Get the profile of the user using the username
    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, user=username)
    # Get the hikes that the user has added
    user_hikes = username.hiking_routes.all()
    return render(
            request, 
            "profiles/profile.html", 
            {"profile":profile,
            "user_hikes": user_hikes,},
            )


def update_profile(request):
    if request.user.is_authenticated:
        profile_form = UpdateProfileForm(data=request.POST or None, instance=request.user.profile)
        if request.method == "POST" and profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, f'Your profile has been updated!')
            return redirect('profile', request.user.username)
    return render(
            request,
            "profiles/update_profile.html",
            {"profile_form":profile_form},
            )
    # else:
    #     messages.add_message(request, messages.ERROR, f'Please login to view this page')
    #     return redirect('hikes')


