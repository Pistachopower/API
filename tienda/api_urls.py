from django.urls import path

from .api_views import *


urlpatterns = [
    path('listar-productos-tercero/', listar_productosTercero),

]