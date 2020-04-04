from satellites.models import Organisation, Satellite, Profile, Suggestion
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from datetime import datetime


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


@login_required(login_url="login")
def signupView(request):
    sats = []
    for sat in Satellite.objects.filter(  # pylint:disable=no-member
        Organisation=request.user.profile.Organisation
    ):
        sats.append(sat.Name)

    if request.method == "POST":
        if request.user.profile.is_head:
            user = dict()
            user["first_name"] = request.POST.get("firstname")
            user["last_name"] = request.POST.get("lastname")
            user["email"] = request.POST.get("email")
            user["password"] = request.POST.get("pswd")
            user["username"] = request.POST.get("username")
            print(user)
            new_user = User(**user)
            try:
                new_user.save()
            except:
                messages.error(request, "Correct the errors in user form !")
                return render(request, "signup2.html", {"sats": sats})
            profile = dict()
            # pylint: disable=no-member
            profile["user"] = User.objects.get(pk=new_user.id)
            profile["phone"] = request.POST.get("phno")
            print(request.POST.get("assat"))
            profile[
                "AssociatedSat"
            ] = Satellite.objects.get(  # pylint: disable=no-member
                pk=request.POST.get("assat")
            )
            profile["EmployeID"] = request.POST.get("eid")
            profile["Address"] = request.POST.get("address")
            profile["Education1"] = request.POST.get("edu1")
            profile["Education1_desc"] = request.POST.get("edu1desc")
            profile["Education2"] = request.POST.get("edu2")
            profile["Education2_desc"] = request.POST.get("edu2desc")
            profile["Education3"] = request.POST.get("edu3")
            profile["Education3_desc"] = request.POST.get("edu3desc")
            profile["Organisation"] = request.user.profile.Organisation
            profile["Profile_pic"] = request.FILES.get("profile_pic")
            profile["WorkExperience"] = request.POST.get("work1")
            profile["WorkExperienceDesc"] = request.POST.get("work1desc")
            new_profile = Profile(**profile)

            try:
                new_profile.save()
            except:
                messages.error(request, "Correct the errors in profile form !")
                return render(request, "signup2.html", {"sats": sats[:5]})
            return redirect("homepage")
        else:
            return render(request, "unauth.html")

    else:
        if request.user.profile.is_head:
            return render(request, "signup2.html", {"sats": sats[:5]})
        else:
            return render(request, "unauth.html")


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


@login_required(login_url="login")
def logoutView(request):
    if request.method == "GET":
        logout(request)
        messages.success(request, "You have been Logged Out !")
        return redirect("homepage")


@login_required(login_url="login")
def generalProfileView(request):
    if request.method == "GET":
        return render(request, "userprofile.html")


@login_required(login_url="login")
def editSatellites(request):
    if request.method == "GET":
        if request.user.profile.is_head:
            return render(request, "sat-index.html")
        else:
            return render(request, "unauth.html")
    elif request.method == "POST":
        if request.user.profile.is_head:
            satellite = dict()
            satellite["Name"] = request.POST.get("satellitename")
            satellite["Organisation"] = request.user.profile.Organisation
            satellite["CountryOrigin"] = request.POST.get("country")
            satellite["Purpose"] = request.POST.get("purpose")
            satellite["ClassOfOrbit"] = request.POST.get("orbitclass")
            satellite["Apogee"] = request.POST.get("apogee")
            satellite["Perigee"] = request.POST.get("perigee")
            satellite["Inclination"] = request.POST.get("inclination")
            satellite["TimePeriod"] = request.POST.get("timeperiod")
            satellite["Power"] = request.POST.get("power")
            satellite["Mass"] = request.POST.get("mass")
            satellite["Picture"] = request.FILES.get("satimage")
            satellite["Description"] = request.POST.get("description")
            satellite["LaunchVehicle"] = request.POST.get("launchvehicle")
            satellite["LifeSpan"] = request.POST.get("lifespan")
            datestr = request.POST.get("launchdate")

            satellite["DateOfLaunch"] = datetime.strptime(datestr, "%d/%m/%Y")
            print(satellite)
            new_sat = Satellite(**satellite)
            try:
                new_sat.save()
                messages.success(request, "Satellite Successfully Saved !")
                return render(request, "sat-index.html")

            except Exception as e:
                print(e)
                messages.error(request, "Please Correct the error !")
                return render(request, "sat-index.html")

        else:
            return render(request, "unauth.html")


def suggestionForm(request):
    if request.method == "POST":
        sug = dict()
        sug["Name"] = request.POST.get("name")
        sug["Email"] = request.POST.get("email")
        sug["Sugestion"] = request.POST.get("suggestion")
        sug["Organisation"] = Organisation.objects.get(
            pk=request.POST.get("organisation")
        )
        current = request.POST.get("current")
        sugi = Suggestion(**sug)
        sugi.save()
        messages.success(request, "Thanks for the feedback")
        return HttpResponseRedirect(current)


@login_required(login_url="login")
def adminProfilePage(request):
    if request.method == "GET":
        if request.user.profile.is_head:
            sugest = Suggestion.objects.filter(
                Organisation__id=request.user.profile.Organisation.id,
                Read=False,
            )

            sugestAll = Suggestion.objects.filter(
                Organisation__id=request.user.profile.Organisation.id
            ).order_by("Read")
            len(sugest)
            sats = Satellite.objects.filter(
                Organisation__id=request.user.profile.Organisation.id
            )
            users = Profile.objects.filter(
                Organisation__id=request.user.profile.Organisation.id
            )
            return render(
                request,
                "admin-prof.html",
                {
                    "notify": len(sugest),
                    "suggests": sugestAll,
                    "sats": sats,
                    "users": users,
                    "satcount": len(sats),
                    "empcount": len(users),
                },
            )
        else:
            return render(request, "unauth.html")
