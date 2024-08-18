from . import views
from django.urls import path

urlpatterns = [
    path('profile/<int:id>', views.profile, name='profile'),
]