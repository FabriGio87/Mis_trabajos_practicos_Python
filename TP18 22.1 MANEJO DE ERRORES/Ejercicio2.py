"""
### Ejercicio 2: Capturando errores de tipo (ValueError)
1. Escribe un programa que solicite al usuario ingresar un número.
2. Intenta convertir el valor ingresado en un número entero.
3. Utiliza `try y except` para capturar el error si el usuario ingresa algo que no es un número, mostrando un mensaje adecuado."""

try:
    numero = int(input("Ingresá un número entero: "))
    print(f"El número ingresado es: {numero}")

except ValueError:
    print("Error: tenés que ingresar un número válido.")