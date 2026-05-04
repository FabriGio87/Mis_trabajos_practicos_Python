"""Ejercicio 3: Uso de if con operadores lógicos or 1. Escribe un programa que solicite al usuario ingresar su edad. 2. Si la edad es menor de 18 **o** mayor de 65, imprime "No estás en el rango permitido para trabajar". 3. Si la edad está entre 18 y 65, imprime "Estás en el rango permitido para trabajar"."""

# 1. Pedir edad
edad = int(input("Ingrese su edad: "))

# 2 y 3. Evaluar con OR
if edad < 18 or edad > 65:
    print("No estás en el rango permitido para trabajar")
else:
    print("Estás en el rango permitido para trabajar")