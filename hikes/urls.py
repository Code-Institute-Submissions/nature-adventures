from . import views
from django.urls import path

urlpatterns = [
    path('', views.HikesList.as_view(), name='hikes'),
]