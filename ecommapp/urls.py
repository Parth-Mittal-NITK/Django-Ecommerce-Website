from django.contrib import admin
from django.urls import path
from ecommapp import views

urlpatterns = [
    path("",views.index, name="index"),
    path("contact",views.contact, name="contact"),
    path("productview/<int:myid>",views.productview, name="productview"), #That <int:myid> lets create a diff page for each produc
    path("checkout",views.checkout, name="checkout"),
    path("tracker",views.tracker, name="tracker"),
    path("address",views.address, name="address"),

]
