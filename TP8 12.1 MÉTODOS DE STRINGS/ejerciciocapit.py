""" Ejercicio 2. Eliminación de espacios y capitalización:
    Tienes la variable `frase = "   hola mundo   "`. Realiza las siguientes operaciones:
    a) Elimina los espacios en blanco al principio y al final de la frase.
    b) Después de eliminar los espacios, capitaliza la primera letra de la frase."""
frase = "   hola mundo   "
# a) Eliminar espacios al inicio y al final
sin_espacios = frase.strip()
# b) Capitalizar la primera letra
capitalizada = sin_espacios.capitalize()
# Mostrar resultados
print(f"Sin espacios: '{sin_espacios}'")
print(f"Capitalizada: '{capitalizada}'")
print(frase.strip().capitalize())