""" Ejercicio  3. Búsqueda de subcadenas:
    Con la variable `texto = "Python es un lenguaje de programación versátil"`:
    a) Encuentra y devuelve la posición de la palabra "lenguaje" en el texto.
    b) Verifica si la palabra "programación" está presente en el texto.(pista: true o False)"""
texto = "Python es un lenguaje de programación versátil"
# Posicón de la palabra "lenguaje"
posicion = texto.find("lenguaje")
# Verificar si la palabra "programación" está presente
existe = "programación" in texto
# Mostrando resultados
print(f"Posición de 'lenguaje': {posicion}") 
print(f"¿Está 'Programación'?:{existe}")