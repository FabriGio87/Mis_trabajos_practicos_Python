"""Ejercicio 4. Reemplazo de caracteres:
    Dada la cadena ‘codigo’ = "Mi código es: 123-ABC-789"`:
    a) Reemplaza todos los guiones ("-") por guiones bajos ("_")."""
codigo = "Mi código es 123-ABC-789"
# Reemplazamos guiones por guiones bajos
nuevo_codigo = codigo.replace("-", "_")
print(nuevo_codigo)