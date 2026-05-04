"""Ejercicio 4: Operaciones con listas
1. Crea una lista `lista1` que contenga varios elementos de diferentes tipos.
2. Usa `append()` para agregar el valor `'hola'` al final de la lista.
3. Usa `insert()` para insertar el valor `'chau'` al inicio de la lista.
4. Elimina el segundo elemento de la lista usando `pop()`.
5. Usa `remove()` para eliminar el primer elemento `'hola'`.
6. Imprime la longitud de la lista, el número de veces que `'hola'` aparece, y la posición de `'hola'` en la lista."""

# 1. Creamos una lista con distintos tipos de variables.
lista1 = [13, "Python", 3.14, True, "familia"]

# 2. Agregamos 'hola' al final
lista1.append("hola")

# 3. Insertar 'chau' al inicio.
lista1.insert(0, "chau")

# 4. Eliminar el segundo elemento (índice 1)
lista1.pop(1)

# 5. Eliminar el primer 'hola'
lista1.remove("hola")

# Tengo que agregar 'hola' de nuevo para poder mostrar count e index, si no tira error.
lista1.append("hola")

# 6. Imprimir datos pedidos
print(f"Lista final: {lista1}")
print(f"Longitud: {len(lista1)}")
print(f"Cantidad de 'hola': {lista1.count('hola')}")
print(f"Posición de 'hola': {lista1.index('hola')}")