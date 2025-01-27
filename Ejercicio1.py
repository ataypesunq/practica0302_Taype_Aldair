'''Crear una Clase Producto con los siguientes atributos:
 - código
 - nombre
 - precio 
Crea su constructor, getter y setter y una función llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.
'''
class Producto:
    def __init__(self, codigo, nombre, precio):
        '''Esta funcion calcula los precios totales de los procductos.
        Parametros:
            - codigo: referencia del producto.
            - nombre: nombre del producto.
            - precio: valor del producto.
        '''
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @codigo.setter
    def codigo(self, valor):
        self.__nombre = valor
    
    @property
    def precio(self):
        return self.__precio

    @codigo.setter
    def codigo(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.precio * unidades

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + 'nombre: ' + self.__nombre + 'precio: ' + str(self.__precio)

    
p1 = Producto(1, "Producto 1", 5)
p2 = Producto(2, "Producto 2", 10)
p3 = Producto(3, "Producto 3", 20)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))