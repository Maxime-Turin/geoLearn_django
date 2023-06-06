from django.shortcuts import render

# Create your views here.


def country_list(request):
    return render(request, 'geoLearn/country_list.html', {})
