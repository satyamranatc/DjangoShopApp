from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductPage, name="ProductPage"),
    path("List/", views.ProductList, name="ProductsList")
]
