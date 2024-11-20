#Ejercicio 5
# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
# luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
# Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

class Fabrica():
  def __init__(self, llantas, color, precio):
    self._llantas=llantas
    self._color=color
    self._precio=precio

class Moto(Fabrica):
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

class Carro(Fabrica):
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

    print("OBJETO=moto")

moto=Moto(2, "Gris", "$200")
moto.cantidad()

print("OBJETO=carro")

carro=Carro(4 ,"Negro", "$600")
carro.cantidad()