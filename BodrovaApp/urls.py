"""django010Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = 'BodrovaApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('abc/<path:path_value>/', views.calculate_z, name='zadacha_1'),
    path('count_overtime/<str:records>/<str:target_day>/', views.count_overtime_entries, name='zadacha_2'),
    path('links/', views.cars_view, name='links'),
    path('our-team/', views.our_team, name='our_team'),
    path('xyz_form/', views.xyz_form, name='xyz_form'),
    path('xyz_result/<int:pk>/', views.xyz_result, name='xyz_result'),
    path('xyz_result_all/', views.xyz_result_all, name='xyz_result_all'),
    path('xyz_result_filtered/', views.xyz_result_filtered, name='xyz_result_filtered'),
    path('stats_view/', views.stats_view, name='stats_view'),
]