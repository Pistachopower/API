from django.urls import path
from .api_views import *



urlpatterns = [
    path('obtener-producto/<int:producto_id>/', obtener_producto, name='obtener_producto'),
    path('listar_productosTercero/', listar_productosTercero, name='listar_productosTercero'),
    path('crear-producto-tercero/', crear_producto_tercero, name='crear_producto_tercero'),
    path('editar-nombre-producto-tercero/<int:producto_id>/', editar_nombre_producto_tercero, name='editar_nombre_producto_tercero'),
    path("eliminar-producto/<int:producto_id>/",eliminar_producto,name="eliminar_producto"),
]