"""### Ejercicio 1: Capturando errores de división por cero
1. Escribe un programa que solicite al usuario ingresar dos números.
2. Intenta dividir el primer número por el segundo.
3. Utiliza `try y except` para manejar la excepción en caso de que el segundo número sea 0 e imprime un mensaje de error."""

# Pedimos dos números al usuario.
numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))

try:
     resultado = numero1 / numero2
     print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
     print("Error: No se puede dividir por cero.5")     