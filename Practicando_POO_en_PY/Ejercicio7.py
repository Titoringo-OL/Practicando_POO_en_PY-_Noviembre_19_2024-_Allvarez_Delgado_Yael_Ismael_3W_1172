#Ejercicio 7
# Desarrollar un programa con tres clases:
# La primera debe ser Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
# La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
# Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad,
#  nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
  def __init__(self,Nombre):
    self.Nombre=Nombre

class Carerra():
  def carrera(self,especialidad):
    self.especialidad=especialidad

class Estudiante(Universidad,Carerra):
  def datos(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad
    print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")

persona=Estudiante("Tec de Juarez")
persona.carrera("Ingeniería mecatronica")
persona.datos("Anthony", 25)