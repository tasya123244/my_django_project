from django.urls import path
from . import views

app_name = 'hse_education'

urlpatterns = [
    path('profile/', views.profile_page, name='profile'),
    path('program/', views.program_page, name='program'),
    path('management/', views.management_page, name='management'),
    path('classmates/', views.classmates_page, name='classmates'),
]