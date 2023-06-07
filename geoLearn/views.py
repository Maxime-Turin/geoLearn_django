from django.shortcuts import render, get_object_or_404, redirect
from .models import Country
from .forms import CountryForm

# Create your views here.


def home_page(request):
    return render(request, 'geoLearn/home_page.html', {})


def country_list(request):
    countries = Country.objects.all().order_by("name")
    return render(request, 'geoLearn/country_list.html', {'countries': countries})


def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'geoLearn/country_detail.html', {'country': country})


def country_new(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm()
    return render(request, 'geoLearn/country_edit.html', {'form': form})


def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm(instance=country)
    return render(request, 'geoLearn/country_edit.html', {'form': form})
