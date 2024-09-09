from django.urls import path
from . import views

urlpatterns = [
    path(
        '<slug:slug>/',
        views.hike_info,
        name='hike_info'),
    path(
        'hikes/create-hike/',
        views.new_hike,
        name='new_hike'),
    path(
        'hikes/update-hike/<slug:slug>/',
        views.update_hike,
        name='update_hike'),
    path(
        'hikes/delete-hike/<slug:slug>/',
        views.delete_hike,
        name='delete_hike'),
    path(
        'like-hike/<slug:slug>/',
        views.like_hike,
        name='like_hike'),
    path(
        '',
        views.HikesList.as_view(),
        name='hikes'),
]
