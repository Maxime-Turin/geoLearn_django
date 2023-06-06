from django.shortcuts import render, get_object_or_404
from .models import Country

# Create your views here.


def home_page(request):
    return render(request, 'geoLearn/home_page.html', {})


def country_list(request):
    countries = Country.objects.all().order_by("name")
    return render(request, 'geoLearn/country_list.html', {'countries': countries})


def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'geoLearn/country_detail.html', {'country': country})
