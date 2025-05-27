from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),   
    path('listar-piezas/', views.listar_pieza_api, name='listar_pieza_api'),
    
]