""" Ejercicio 1: Uso de `round()` y `abs()`
1. Declara un número decimal negativo `num1` y con 4 dígitos decimales. 
2. Usa la función `abs()` para obtener el valor absoluto de `num1` y almacénalo en una nueva variable.
3. Usa la función `round()` para redondear el valor absoluto a 2 decimales.
4. Imprime el resultado de esta última."""

# 1. Declaramos número decimal negativo.
num1 = -12.3456

# 2. Valor absoluto.
valor_absoluto = abs(num1)

# 3. Redondear a 2 decimales.
redondeado = round(valor_absoluto, 2)

# 4. Imprimir el resultado final.
print(f"Resultado final: {redondeado}")