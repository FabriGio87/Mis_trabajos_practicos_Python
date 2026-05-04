""" Ejercicio 5: Reemplazo de caracteres en la concatenación
1. Declara dos variables `var1` y `var2` como strings.
2. Crea una variable `var3` que concatene el primer carácter de `var1` con el segundo carácter de `var2`, usando una f-string.
3. Imprime el valor de `var3`."""
# a) Declaramos las variables
var1 = "Hola"
var2 = "mundo"
# b) Creamos tercer variable y concatenamos
var3 = f"{var1[0]}{var2[1]}"
# c) Imprimimos el resultado
print(var3)