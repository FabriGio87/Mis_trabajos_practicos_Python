"""### Ejercicio 4: Intento de modificación y uso de slicing
1. Crea una tupla `datos` con al menos 5 elementos.
2. Intenta cambiar el valor del segundo elemento y observa el error que genera (ya que las tuplas son inmutables).
3. Usa rebanado para extraer los primeros tres elementos de la tupla e imprímelos. """

# 1. Creamos una tupla.
datos = (10, 20, 30, 40, 50)

# 2. Intentamos modificar el segunod elemento (sabiendo que va a fallar).
# datos[1] = 13 #

# 3. Extraer los primeros tres elementos.
subtupla = datos[:3]

# Imprimimos el resultado.
print("Subtupla: ", subtupla)