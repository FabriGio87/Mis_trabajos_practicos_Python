""" Ejercicio 2: Sublistas y rebanado
1. Crea una lista `numeros` con los valores `[10, 20, 30, 40, 50, 60]`.
2. Extrae una sublista que contenga los elementos desde el índice 2 hasta el 4 (sin incluir el índice 4).
3. Extrae una sublista que contenga los primeros 5 elementos.
4. Imprime ambas sublistas."""

# 1. Creamos una lista de números.
numeros = [10, 20, 30 , 40, 50, 60]

# 2. Sublista N° 1; desde índice 2 hasta 4 (sin incluir 4).
sublista1 = numeros[2:4]

# 3. Sublista N° 2; primeros 5 elementos.
sublista2 = numeros[:5]

# 4. Imprimimos ambas sublistas.
print(f"Sublista 1: {sublista1}")
print(f"Sublista 2: {sublista2}")