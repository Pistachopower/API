from .models import *
from .serializers import *


from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
import requests 
from django.core import serializers
from django.shortcuts import render



@api_view(['GET'])
def listar_productosTercero(request):    
    listaProductosTercero = ProductosTerceros.objects.all()
    serializer = ProductoTerceroSerializer(listaProductosTercero, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_producto_tercero(request):
    
    productoTercero = ProductoTerceroCreateSerializer(data=request.data)
    
    if productoTercero.is_valid():
        productoTercero.save()
        return Response("Creado producto tercero")
        
    else:
        return Response(
            productoTercero.errors, status=status.HTTP_400_BAD_REQUEST
        )