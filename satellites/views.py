from satellites.forms import ProfileForm, UserForm
from satellites.models import Satellite, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def homepageView(request):
    satellites = Satellite.objects.all()[:24]  # pylint: disable=no-member
    page = request.GET.get("page", 1)

    paginator = Paginator(satellites, 6)

    try:
        satellites = paginator.page(page)
    except PageNotAnInteger:
        satellites = paginator.page(1)
    except EmptyPage:
        satellites = paginator.page(paginator.num_pages)

    return render(request, "homepage.html", {"satellites": satellites})


def descriptionView(request, name):
    sat = Satellite.objects.get(pk=name)  # pylint: disable=no-member

    return render(request, "description.html", {"satellite": sat})


def fullimageView(request, name):
    sat = Satellite.objects.get(pk=name)  # pylint: disable=no-member
    return render(request, "fullimage.html", {"satellite": sat})


def signupView(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()

            data = dict()
            data["user"] = user
            data["phone"] = profile_form["phone"].value()
            data["EmployeID"] = profile_form["EmployeID"].value()
            # pylint: disable=no-member
            data["AssociatedSat"] = Satellite.objects.get(pk=profile_form["AssociatedSat"].value())
            data["WorkExperience"] = profile_form["WorkExperience"].value()
            data["Education"] = profile_form["Education"].value()
            prof = Profile(**data)
            prof.save()
            user = authenticate(username=user.username, password=user_form.cleaned_data.get("password1"))
            login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, "Incorrect Credentials !")
            user_form = UserForm()
            profile_form = ProfileForm()
            return render(request, "extend.html", {"user_form": user_form, "profile_form": profile_form})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request, "extend.html", {"user_form": user_form, "profile_form": profile_form})


@csrf_exempt
def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("Password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request, "login.html")

    else:
        return render(request, "login.html")


@login_required
def logoutView(request):
    if request.method == "GET":
        logout(request)
        messages.success(request, "You have been Logged Out !")
        return redirect("homepage")


# @login_required
# def editSatellites(request):
