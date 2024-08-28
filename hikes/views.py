from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.template.defaultfilters import slugify
from .models import Hike
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

    return render(
        request,
        "hikes/hike_info.html",
        {"hike": hike},
    )


# Create a new hike
def new_hike(request):
    if request.user.is_authenticated:
        hike_form = CreateHikeForm(data=request.POST)
        if request.method == "POST" and hike_form.is_valid():
            added_hike = hike_form.save(commit=False)
            # Add the current user as the author
            added_hike.author = request.user
            # Add slugified hike_name as the slug
            added_hike.slug = slugify(added_hike.hike_name)
            added_hike.save()
            return redirect('hikes')
    return render(
        request,
        "hikes/create_hike.html",
        {"hike_form":hike_form,}
    )


        
