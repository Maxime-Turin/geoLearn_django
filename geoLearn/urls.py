from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('country_list/', views.country_list, name='country_list'),
    path('country/<int:pk>/', views.country_detail, name='country_detail'),
    path('country/new/', views.country_new, name='country_new'),
    path('country/<int:pk>/edit/', views.country_edit, name='country_edit')
]
