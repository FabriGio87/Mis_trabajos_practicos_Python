"""Ejercicio 4: Uso de if con operadores lógicos and1. Escribe un programa que solicite al usuario ingresar dos números.2. Si ambos números son positivos, imprime "Ambos números son positivos".3. Si alguno de los dos números es negativo o cero, imprime "No ambos números son positivos"."""

# 1. Pedir dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# 2 y 3. Evaluar con AND
if num1 > 0 and num2 > 0:
    print("Ambos números son positivos")
else:
    print("No ambos números son positivos")