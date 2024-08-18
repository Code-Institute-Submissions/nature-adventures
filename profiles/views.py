from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

@login_required
def profile(request, id):
    queryset = Profile.objects.all()
    profile = get_object_or_404(queryset, id=id)
    return render(
            request, 
            "profiles/profile.html", 
            {"profile":profile}
            )