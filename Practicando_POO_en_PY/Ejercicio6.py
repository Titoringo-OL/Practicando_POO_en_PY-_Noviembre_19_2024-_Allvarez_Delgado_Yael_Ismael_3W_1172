#Ejercicio 6
# Crear una clase llamada Marino(), con un método que sea hablar, 
# en donde muestre un mensaje que diga «Hola, soy un animal marino!». 
# Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por «Hola soy un Pulpo!».
# Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parámetro.

class Marino():
  def hablar(self):
    print("Hola soy un animal marino!")

class Pulpo(Marino):
  def hablar(self):
    print("Hola soy un pulpo!")

class Foca(Marino):
  def hablar(self,mensaje):
    self.mensaje=mensaje
    print(mensaje)

marino=Marino()
marino.hablar()

pulpo=Pulpo()
pulpo.hablar()

foca=Foca()
foca.hablar("Hola soy una foca!")