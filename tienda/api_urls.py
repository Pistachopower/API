from django.urls import path
from .api_views import *



urlpatterns = [
    path('listar_productosTercero/', listar_productosTercero, name='listar_productosTercero'),
    path('crear-producto-tercero/', crear_producto_tercero, name='crear_producto_tercero'),


]