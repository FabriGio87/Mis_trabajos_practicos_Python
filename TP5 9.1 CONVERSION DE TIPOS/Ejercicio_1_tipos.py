'''1. Escribe un programa que pida al usuario su nombre y edad, y luego imprima un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años". Utiliza la función type para verificar que el tipo de dato de la edad es un entero.'''
# Pedir datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
# Verificar el tipo de dato de edad
print(type(edad))
# Mostrar mensaje
print(f"¡Hola, {nombre}! Tienes {edad} años")