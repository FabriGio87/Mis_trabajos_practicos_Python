"""Ejercicio 1. Conversión de mayúsculas y minúsculas:
    Dada la variable `nombre = "juan carlos"`, utiliza los métodos de strings para:
    a) Convertir todo el nombre a mayúsculas.
    b) Convertir todo el nombre a minúsculas.
    c) Convertir el nombre a formato de título (primera letra de cada palabra en mayúscula)."""
nombre = "juan carlos"
# a) Todo en mayúsculas
mayusculas = nombre.upper()
# b) Todo en minúsculas
minusculas = nombre.lower()
# c) Formato título
titulo = nombre.title()
# Mostrar resultados
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")
print(f"Título: {titulo}")