""" Ejercicio 3: Combinación de operaciones con números enteros y decimales
1. Declara un número entero `num_entero` y un número decimal `num_decimal`.
2. Realiza las siguientes operaciones entre ellos: suma, resta, multiplicación, y módulo.
3. Usa el operador `+=` para sumar el resultado de la multiplicación a `num_entero`.
4. Imprime los resultados de cada paso."""

# 1. Declaramos las variables.
num_entero = 9
num_decimal = 4.5
print(f" Valores Iniciales - Entero: {num_entero}, Decimal: {num_decimal}")

# 2. Operaciones
suma = num_entero + num_decimal
resta = num_entero - num_decimal
multiplicacion = num_entero * num_decimal
modulo = num_entero % num_decimal

print(f"Suma : {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"Módulo: {modulo}")

# 3. Usar += con la multiplicación
num_entero += multiplicacion

# 4. Mostrar resultado final
print(f"Nuevo valor de num_entero después de += multiplicación: {num_entero}")