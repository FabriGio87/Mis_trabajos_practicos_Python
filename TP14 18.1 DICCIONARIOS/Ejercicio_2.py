"""### Ejercicio 2: Eliminación de un elemento en el diccionario
1. Crea un diccionario `colores` que tenga al menos tres pares clave-valor relacionados con colores.
2. Elimina el par con la clave `'azul'` usando `del()`.
3. Imprime el diccionario antes y después de la eliminación."""

# 1. Crear el diccionario
colores = {'rojo': 'red','azul': 'blue','verde': 'green'}

# Mostrar antes
print("Antes:", colores)

# 2. Eliminar la clave 'azul'
del colores['azul']

# 3. Mostrar después
print("Después:", colores)