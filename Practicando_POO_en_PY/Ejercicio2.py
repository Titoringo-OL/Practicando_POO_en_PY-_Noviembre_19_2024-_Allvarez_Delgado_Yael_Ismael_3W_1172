#Ejercicio 2
# Crea una clase “Persona”. Con atributos nombre y edad. 
# Además, hay que crear un método “cumpleaños”, que aumente en 1 
# la edad de la persona cuando se invoque sobre un objeto creado con “Persona”.
# Tendríamos que lograr ejecutar el siguiente código con la clase creada:

class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Solicitar el nombre y la edad al usuario
nombre = input("Ingrese nombre: ")
while True:
    try:
        edad = int(input("Ingrese edad: "))
        break  # Sale del ciclo si la edad es válida
    except ValueError:
        print("Por favor ingrese un número válido para la edad.")

# Crear el objeto Persona con los datos ingresados
p = Persona(nombre, edad)
p.cumpleaños()  # Llamada a cumpleaños para aumentar la edad en 1
p.cumpleaños()  # Llamada a cumpleaños nuevamente

# Imprimir el resultado
print(f"{p.nombre} cumple {p.edad} años")
