"""Ejercicio 4: Cadenas vacías y concatenación
1. Declara dos variables `var1` y `var2`, donde `var1` es un string vacío y `var2` contiene un texto.
2. Concatenar ambas usando f-string y almacena el resultado en `var3`.
3. Imprime el valor de `var3` y verifica que no hay espacios extra."""
# a) Declaramos las variables
var1 = ""
var2 = "Hola mundo"
# b) Concatenamos con f-string
var3 = f"{var1}{var2}"
# c) Imprimimos el resultado
print(var3)