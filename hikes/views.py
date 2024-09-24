from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Hike, Like
from .forms import CreateHikeForm


class HikesList(generic.ListView):
    """
    Returns all added hikes in :model:`hikes.Hike`
    and displays 3 hikes per page.

    **Context**

    ``queryset``
        All instances of :model:`hikes.Hike` ordered by the number of likes
    ``context_object_name``
        User-friendly name of the object returned
    ``paginate_by``
        Number of posts per page

    **Template**

    :template:`hikes/hikes_list.html`
    """
    queryset = Hike.objects.annotate(
        likes=Count('hike_likes')
    ).order_by('-likes')
    template_name = "hikes/hikes_list.html"
    context_object_name = "hikes_list"
    paginate_by = 3


def hike_info(request, slug):
    """
    Display an individual :model:`hikes.Hike`.

    **Context**

    ``hike``
    An instance of :model:`hikes.Hike`.
    ``likes``
    A count of all likes the hike has received
    ``liked_hike``
    A list of users who have liked the hike
    ``previous_url``
    Previous/referring URL

    **Template**

    :template:`hikes/hike_info.html`
    """

    queryset = Hike.objects.all()
    hike = get_object_or_404(queryset, slug=slug)
    # Count the number of times the hike has been liked
    likes = Like.objects.filter(hike=hike).count()

    # Create a list of users who have liked the hike
    # How to use values list and flat taken from:
    # https://stackoverflow.com/questions/37205793/
    # django-values-list-vs-values
    liked_hike = list(
        Like.objects.filter(hike=hike).values_list(
            "user__username",
            flat=True)
    )
    # Get the url of the previous page the user was on
    previous_url = request.META.get('HTTP_REFERER')

    return render(
        request,
        "hikes/hike_info.html",
        {"hike": hike,
         "likes": likes,
         "liked_hike": liked_hike,
         "previous_url": previous_url, },
    )


@login_required
def new_hike(request):
    """
    Allow user to add a new hike

    **Context**

    ``hike_form``
        An instance of of :form:`hikes.CreateHikeForm`

    ** Template **

    :template:`hikes/create.hike.html`
    """
    if request.user.is_authenticated:
        hike_form = CreateHikeForm(
            data=request.POST or None,
            files=request.FILES or None
        )
        if request.method == "POST":
            if hike_form.is_valid():
                added_hike = hike_form.save(commit=False)
                # Check that the hike name contains letters
                name_valid = False
                for char in added_hike.hike_name:
                    if char.isalpha():
                        name_valid = True
                if name_valid == True:
                    # Add the current user as the author
                    added_hike.author = request.user
                    # Add slugified hike_name as the slug
                    added_hike.slug = slugify(added_hike.hike_name)
                    added_hike.save()
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Your hiking route has been added successfully!')
                    return redirect('hike_info', added_hike.slug)
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        'The hike name needs to contain letters'
                    )
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'There has been an error, please try again.'
                )
    return render(
        request,
        "hikes/create_hike.html",
        {"hike_form": hike_form, }
    )


@login_required
def update_hike(request, slug):
    """
    Display :form:`hikes.CreateHikeForm` for edit.

    ** Context **

    ``selected_hike``
        An instance of :model:`hikes.Hike`
    ``update_form``
        An instance of :form:`hikes.CreateHikeForm`

    **Template**

    :template:`hikes/update_hike.html`
    """
    selected_hike = get_object_or_404(Hike, slug=slug)
    update_form = CreateHikeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=selected_hike
    )
    if request.method == "POST":
        if update_form.is_valid():
            updated_hike = update_form.save(commit=False)
            updated_hike.slug = slugify(updated_hike.hike_name)
            updated_hike.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your hiking route has been updated successfully!')
            return redirect('hike_info', selected_hike.slug)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating the hike. Please try again'
            )
    return render(
        request,
        "hikes/update_hike.html",
        {"selected_hike": selected_hike,
         "update_form": update_form}
    )


@login_required
def delete_hike(request, slug):
    """
    Delete a hike.

    **Context**

    ``selected_hike``
        An instance of :model:`hikes.Hike`
    """
    if request.user.is_authenticated:
        selected_hike = get_object_or_404(Hike, slug=slug)
        if request.user == selected_hike.author:
            selected_hike.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your hiking route has been deleted successfully!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error has occured. Please try again.')
    return HttpResponseRedirect(reverse('hikes'))


@login_required
def like_hike(request, slug):
    """
    Like or unlike a hike.

    """
    if request.user.is_authenticated:
        hike = get_object_or_404(Hike, slug=slug)
        # If the user is not the hike author allow to like/unlike the hike
        # https://stackoverflow.com/questions/51206549/django-create-or-delete-object
        if request.user != hike.author:
            # Check whether the user has already liked the post and
            # if so, unlike the hike
            try:
                Like.objects.get(user=request.user, hike=hike).delete()
            # If the Like does not exist, create a like
            except Like.DoesNotExist:
                Like.objects.create(user=request.user, hike=hike)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'You cannot like your own route!')
        return redirect('hike_info', hike.slug)
