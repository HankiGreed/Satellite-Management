from django.contrib import admin
from django.urls import path, include
from .views import homepageView, descriptionView, fullimageView

urlpatterns = [
    path("", homepageView, name="homepage"),
    path("description/<str:name>/", descriptionView, name="description"),
    path("full/<str:name>/", fullimageView, name="full"),
]
