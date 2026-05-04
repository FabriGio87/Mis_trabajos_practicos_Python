"""Ejercicio 1: Creación, modificación y acceso a listas
1. Crea una lista `lista` que contenga al menos 5 elementos, incluyendo diferentes tipos de datos (enteros, cadenas, booleanos, etc.).
2. Accede al último elemento de la lista usando índices negativos.
3. Modifica el tercer elemento de la lista y cámbialo por la cadena `'chau'`"""

# 1. Creamos una lista con distintos tipos de datos.
lista = [13, 'Hola', False, 3.14, 'Python']

# 2. Accedemos al último elemento de la lista.
print(f"Último elemento de la lista: {lista[-1]}")

# 3. Modificar el tercer elemento de la lista.
lista[2] = 'chau'
print(f"Lista modificada: {lista}")