"""### Ejercicio 2: Iterando sobre un diccionario con `items()`
1. Crea un diccionario que contenga tres elementos clave-valor, donde las claves sean nombres de frutas y los valores sean sus colores.
2. Usa un bucle `for` para iterar sobre los elementos del diccionario e imprime tanto la fruta como su color en formato "Fruta: color"."""

# Crear el diccionario
frutas = {"manzana": "roja", "banana": "amarilla", "pera": "verde"}

# Iterar con items
for fruta, color in frutas.items():
    print(f"{fruta}: {color}")