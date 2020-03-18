from satellites.models import Satellite
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepageView(request):
    satellites = Satellite.objects.all()[:24]
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
    sat = Satellite.objects.get(pk=name)

    return render(request, "description.html", {"satellite": sat})


def fullimageView(request, name):
    sat = Satellite.objects.get(pk=name)
    return render(request, "fullimage.html", {"satellite": sat})
