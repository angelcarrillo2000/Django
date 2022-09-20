
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('departamentos', views.Departamentos, name='departamentos'),
    path('personas/', views.personas, name='personas'),
    path('personas/crear', views.crear, name='crear'),
    path('personas/editar/', views.editar, name='editar'), 
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), 
    path('personas/editar/<int:id>', views.editar, name='editar'), 
     
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)