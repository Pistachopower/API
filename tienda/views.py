from django.shortcuts import render

import requests 
from django.core import serializers


def index(request):
    return render(request, "index.html")

def listar_pieza_api(request):
    headers= {
        'Authorization': 'Bearer IpUM35wKSdi0lK0Lc16nlmEC0wa1ug'
    }
    
    #datos de la API
    response = requests.get('http://0.0.0.0:8000/api/v1/listar_piezas/',
                            headers=headers)
    
    #transformar los datos a un formato JSON
    listar_pieza_api = response.json()
    
    return render(request, 'piezas/listar_pieza_api.html', {'listar_pieza_api': listar_pieza_api})
    
    



    
