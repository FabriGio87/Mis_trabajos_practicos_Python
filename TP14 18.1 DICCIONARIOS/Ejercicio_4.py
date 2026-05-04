"""### Ejercicio 4: Lista de diccionarios 1. Crea una lista vacía llamada lista_de_dicc. 2. Agrega el diccionario auto (del ejercicio anterior) a la lista usando append(). 3. Accede e imprime el valor de la clave 'modelo' del primer diccionario en la lista."""

# (Usamos el diccionario auto del ejercicio anterior)
auto = {'marca': 'Toyota','modelo': 'Corolla','año': 2020,'precio': {'pesos': 8500000,'dolares': 10000}}

# 1. Crear lista vacía
lista_de_dicc = []

# 2. Agregar el diccionario a la lista
lista_de_dicc.append(auto)

# 3. Acceder al 'modelo' del primer diccionario
print("Modelo:", lista_de_dicc[0]['modelo'])