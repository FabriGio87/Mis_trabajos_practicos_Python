"""Ejercicio 1: Uso básico de if y else  1. Escribe un programa que solicite al usuario ingresar un número.2. Si el número es positivo, imprime "El número es positivo".3. Si el número es negativo o igual a cero, imprime "El número es negativo o cero"."""

# 1. Pedir número
numero = float(input("Ingrese un número: "))

# 2 y 3. Condición
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo o cero")