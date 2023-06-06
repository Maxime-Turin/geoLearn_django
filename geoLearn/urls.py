from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('country_list/', views.country_list, name='country_list'),
    path('country/<int:pk>/', views.country_detail, name='country_detail'),
]
