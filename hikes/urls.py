from . import views
from django.urls import path

urlpatterns = [
    path('', views.HikesList.as_view(), name='hikes'),
    path('<slug:slug>/', views.hike_info, name='hike_info'),
]