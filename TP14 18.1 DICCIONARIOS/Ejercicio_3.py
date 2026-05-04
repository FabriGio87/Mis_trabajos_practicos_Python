"""### Ejercicio 3: Diccionario dentro de otro diccionario
1. Crea un diccionario `auto` que contenga información sobre un vehículo con las claves `'marca'`, `'modelo'`, `'año'`, y un diccionario anidado para `'precio'` que incluya `'pesos'` y `'dolares'`.
2. Accede e imprime el valor del precio en dólares del auto.
3. Modifica el valor del precio en pesos y vuelve a imprimir el diccionario."""

# 1. Crear el diccionario con uno anidado
auto = {'marca': 'Toyota','modelo': 'Corolla','año': 2020,'precio': {'pesos': 8000000,'dolares': 10000}}

# 2. Acceder al precio en dólares
print("Precio en dólares:", auto['precio']['dolares'])

# 3. Modificar el precio en pesos
auto['precio']['pesos'] = 8500000

# Mostrar diccionario actualizado
print("Diccionario actualizado:", auto)