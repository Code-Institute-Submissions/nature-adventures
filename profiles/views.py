from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.defaultfilters import slugify
from .models import Profile
from .forms import UpdateProfileForm
from hikes.models import Like

# Create your views here.


@login_required
def profile(request, username):
    """
    Renders profile information about the selected user.

    **Context**

    ``profile``
        An instance of :model:`profiles.Profile`
    ``user_hikes``
        All hikes that the user has added
    ``user_likes``
        A list of hikes that the user has liked

    **Template**

    :template:`profiles/profile.html`
    """
    users = User.objects.all()
    username = get_object_or_404(users, username=username)
    # Get the profile of the user using the username
    profiles = Profile.objects.all()
    profile = get_object_or_404(profiles, user=username)
    # Get the hikes that the user has added
    user_hikes = username.hiking_routes.all()
    # Get the hikes the user has liked
    user_likes = list(
        Like.objects.filter(user=username).values_list(
            "hike__hike_name",
            flat=True)
    )
    return render(
        request,
        "profiles/profile.html",
        {"profile": profile,
         "user_hikes": user_hikes,
         "user_likes": user_likes, },
    )


@login_required
def update_profile(request):
    """
    Update user profile information.

    **Context**

    ``profile_form``
        An instance of :form:`profiles.UpdateProfileForm`

    **Template**

    :template:`profiles/update_profile.html`
    """
    profile_form = UpdateProfileForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=request.user.profile
    )
    if request.method == "POST":
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'Your profile has been updated!'
            )
            return redirect('profile', request.user.username)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                f'Something went wrong, please try again.'
            )
            return redirect('profile', request.user.username)
    return render(
        request,
        "profiles/update_profile.html",
        {"profile_form": profile_form},
    )
