from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests 
from django.core import serializers
from django.shortcuts import render

@api_view(['GET'])
def listar_productosTercero(request):
    listaProductosTercero = ProductosTerceros.objects.all()
    serializer = ProductoTerceroSerializer(listaProductosTercero, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listar_productosTercero(request):
    headers= {
        'Authorization': 'Bearer uXeCuCqzq8w2MksxlV4DPBhfYzx8qU'
    }
    
    #datos de la API
    response = requests.get('http://0.0.0.0:8081/api/v1/listar-productos-tercero/',
                            headers=headers)
    
    #transformar los datos a un formato JSON
    listar_productosTercero_Api = response.json()
    
    return render(request, 'productosTercero/listar_productosTercero_api.html', {'listar_productosTercero_Api': listar_productosTercero_Api})
