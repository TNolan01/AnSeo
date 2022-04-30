from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('players/',views.players),
    path('training/',views.training),
]