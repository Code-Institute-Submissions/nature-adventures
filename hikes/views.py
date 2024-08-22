from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Hike

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
