from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('profiles/update_profile/', views.update_profile, name='update_profile'),
]