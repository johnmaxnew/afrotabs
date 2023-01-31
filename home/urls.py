from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_index, name="home_index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("cookie/", views.cookie, name="cookie"),
]
