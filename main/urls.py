from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:car_id>", views.delete, name="delete"),
    path("edit_form/<int:car_id>", views.edit_form, name="edit_form"),
    path("edit_htmx/<int:car_id>", views.edit_htmx, name="edit_htmx"),
    path("accounts/", include("allauth.urls"))
]