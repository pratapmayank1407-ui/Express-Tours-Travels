from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("packages/", views.packages, name="packages"),
    path("packages/<int:pk>/", views.package_detail, name="package_detail"),
    path("book/", views.book, name="book"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]
