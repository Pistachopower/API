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
    
    #Usamos validate de django para sobreescribir la validación de los campos
    #data: son los datos que vienen del cliente
    # def validate(self, data):
    #     vendedor_id = data.get('vendedor')
    #     producto_id = data.get('producto_id')

    #     # Validar que el producto existe
    #     producto = ProductosTerceros.objects.filter(id=producto_id).first()
    #     if not producto:
    #         raise serializers.ValidationError("El producto no existe.")

    #     # Validar que el vendedor coincide con algo del producto, si es necesario
    #     if producto.vendedor_id != vendedor_id:
    #         raise serializers.ValidationError("El vendedor no corresponde con el producto.")

    #     return data
    
    
class ProductoTerceroActualizarSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ProductosTerceros
        fields = '__all__'
        
    def validate_nombre(self, nombre):
    # validamos que la pieza existe
        # compruebaPieza = ProductosTerceros.objects.filter(nombre=nombre).first()
        # if compruebaPieza is None:
        #     raise serializers.ValidationError('La pieza no existe')
        
        
        if self.instance.nombre == nombre:
            raise serializers.ValidationError('El nombre no ha cambiado')
        return nombre
    
    #self: mi registro de la bd
    def validate(self, data):
        
        if self.instance:
            nuevo_nombre = data.get('nombre')
            vendedor = data.get('vendedor', self.instance.vendedor)
           
            if nuevo_nombre and nuevo_nombre != self.instance.nombre:
                
                if vendedor != self.instance.vendedor:
                    raise serializers.ValidationError(
                        {"nombre": "No puedes cambiar el nombre si no eres el propietario actual."}
                    )
        return data
        
        
        
        
        