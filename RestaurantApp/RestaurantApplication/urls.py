from django.urls import path

from .views import *

urlpatterns = [
    path('home', homePage, name='Home'),
    path('login', utilisateur_login, name='Login'),
    path('register', utilisateur_register, name='Register'),
    path('restaurant', listRestaurant, name='Restaurant'),
    path('noteRestaurant', get_note_restaurant, name='NoteRestaurant'),




]
