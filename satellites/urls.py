from os import name
from django.contrib import admin
from django.urls import path, include
from .views import (
    adminProfilePage,
    editSatellites,
    editUserView,
    generalProfileView,
    homepageView,
    descriptionView,
    fullimageView,
    loginView,
    logoutView,
    signupView,
    suggestionForm,
)

urlpatterns = [
    path("", homepageView, name="homepage"),
    path("description/<str:name>/", descriptionView, name="description"),
    path("full/<str:name>/", fullimageView, name="full"),
    path("signup", signupView, name="signup"),
    path("login", loginView, name="login"),
    path("logout", logoutView, name="logout"),
    path("profile", generalProfileView, name="userprofile"),
    path("editsat", editSatellites, name="editsat"),
    path("suggest", suggestionForm, name="suggest"),
    path("adminprof", adminProfilePage, name="adminprofile"),
    path("edituser/<int:id>", editUserView, name="edituser"),
]
