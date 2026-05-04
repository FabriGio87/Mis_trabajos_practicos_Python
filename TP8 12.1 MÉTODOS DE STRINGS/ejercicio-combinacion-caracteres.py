""" Ejercicio  5. Combinación de métodos:
    Tienes la variable `entrada = "  PYTHON ES GENIAL  "`. Realiza las siguientes operaciones en orden:
    a) Elimina los espacios en blanco al principio y al final.
    b) Convierte todo el texto a minúsculas.
    c) Reemplaza la palabra "python" por "JavaScript".
    d) Imprime el resultado final."""
entrada = "  PYTHON ES GENIAL  "
# a) Eliminar espacios
resultado = entrada.strip()
# b) Pasar a minúsculas
resultado = resultado.lower()
# c) Reemplazar "python" por "JavaScript"
resultado = resultado.replace("python", "JavaScript")
# d) Mostrar resultado
print(resultado)
print(entrada.strip().lower().replace("python", "JavaScript"))