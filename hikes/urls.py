from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.hike_info, name='hike_info'),
    path('hikes/create-hike/', views.new_hike, name='new_hike'),
    path('hikes/update-hike/<slug:slug>/', views.update_hike, name='update_hike'),
    path('', views.HikesList.as_view(), name='hikes'),
]