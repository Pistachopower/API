from rest_framework import serializers
from .models import *

class ProductoTerceroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosTerceros
        fields = '__all__'
        
        
class ProductoTerceroCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosTerceros
        fields = '__all__'
        
        
    def validate_nombre(self, nombre):
        # value es el nombre recibido
        compruebaPieza = ProductosTerceros.objects.filter(nombre=nombre).first()
        if compruebaPieza is not None:
            raise serializers.ValidationError('Ya existe una pieza con ese nombre')
        return nombre