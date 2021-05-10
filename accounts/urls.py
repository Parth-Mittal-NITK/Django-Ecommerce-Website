from django.contrib import admin
from django.urls import path
from accounts import views

#These only map a url to a method in views.py. Even if an HTML file doesnt exist for that
#particualr function, its ok if it serves the purpose
#An example is logout which doesnt have a logout.html file
urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"), 
    path("profile", views.profile, name="profile"), 
    path("edit_profile", views.edit_profile, name="edit_profile"), 
]
