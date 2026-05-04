"""Ejercicio 3: Concatenación y acceso a caracteres
1. Declara dos variables `var1` y `var2` como strings.
2. Usa una f-string para concatenar el segundo carácter de `var1` con el primer carácter de `var2` en una nueva variable `var3`.
3. Imprime el valor de `var3`."""
# a) Declaramos las variables
var1 = "Hola"
var2 = "Mundo"
# b) Tomamos caracteres y concatenamos con f-string
var3 = f"{var1[1]}{var2[0]}"
# c) Imprimimos el resultado
print(var3)