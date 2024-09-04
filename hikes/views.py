from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Hike, Like
from .forms import CreateHikeForm

# Create your views here.

# Display a list view of all the added hikes
class HikesList(generic.ListView):
    queryset = Hike.objects.all()
    template_name = "hikes/hikes_list.html"
    context_object_name = "hikes_list"
    paginate_by = 3


# Display detailed information about the selected hike
def hike_info(request, slug):
    """
    Display an individual :model:`hikes.Hike`.

    **Context**

    ``hike``
    An instance of :model:`hikes.Hike`.

    **Template**

    :template:`hikes/hike_info.html`
    """

    queryset = Hike.objects.all()
    hike = get_object_or_404(queryset, slug=slug)
    #Count the number of times the hike has been liked
    likes = Like.objects.filter(hike=hike).count()

    return render(
        request,
        "hikes/hike_info.html",
        {"hike": hike,
        "likes": likes},
    )


# Create a new hike
def new_hike(request):
    if request.user.is_authenticated:
        hike_form = CreateHikeForm(data=request.POST or None, files=request.FILES or None)
        if request.method == "POST":
            if hike_form.is_valid():
                added_hike = hike_form.save(commit=False)
                # Add the current user as the author
                added_hike.author = request.user
                # Add slugified hike_name as the slug
                added_hike.slug = slugify(added_hike.hike_name)
                added_hike.save()
                messages.add_message(request, messages.SUCCESS, f'Your hiking route has been added successfully!')
                return redirect('hike_info', added_hike.slug)
    return render(
        request,
        "hikes/create_hike.html",
        {"hike_form":hike_form,}
    )


# Update a hike
def update_hike(request, slug):
    if request.user.is_authenticated:
        selected_hike = get_object_or_404(Hike, slug=slug)
        update_form = CreateHikeForm(data = request.POST or None, files=request.FILES or None, instance = selected_hike)
        if request.method == "POST":    
            if update_form.is_valid():
                update_form.save()
                return redirect('hike_info', selected_hike.slug)
    return render(
        request,
        "hikes/update_hike.html",
        {"selected_hike":selected_hike,
        "update_form":update_form}
    )


# Delete a hike
def delete_hike(request, slug):
    if request.user.is_authenticated:
        selected_hike = get_object_or_404(Hike, slug=slug)
        if request.user == selected_hike.author:
            selected_hike.delete()
            messages.add_message(request, messages.SUCCESS, f'Your hiking route has been deleted successfully!')
    return HttpResponseRedirect(reverse('hikes'))


# Like a Hike or remove a Like
def like_hike(request, slug):
    if request.user.is_authenticated:
        hike = get_object_or_404(Hike, slug=slug)
        user = request.user
        # https://stackoverflow.com/questions/51206549/django-create-or-delete-object
        try:
            Like.objects.get(user=user, hike=hike).delete()
        except Like.DoesNotExist:
            Like.objects.create(user=user, hike=hike)
        return redirect('hike_info', hike.slug)
