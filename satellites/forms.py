from django import forms
from satellites.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("user", "phone", "EmployeID", "AssociatedSat", "Address", "WorkExperience", "Education")
        widgets = {"user": forms.HiddenInput()}
