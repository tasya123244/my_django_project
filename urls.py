from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from BodrovaApp import views as bodrova_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BodrovaApp/', include('BodrovaApp.urls', namespace='BodrovaApp')),
    path('hse/', include('hse_education.urls')),
    
    path('', bodrova_views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)