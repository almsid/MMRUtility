
from django.urls import path

from MMRUtilityApp import views

urlpatterns = [
    path("", views.index, name="index"),
]