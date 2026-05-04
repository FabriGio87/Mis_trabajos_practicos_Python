"""Ejercicio 2: Uso de `ceil()` y `floor()`
1. Usa `import math` para importar el módulo de matemáticas.
2. Declara una variable con un número decimal `num2`, usando input (Recuerda aplicarle el método float())
3. Usa las funciones `ceil()` y `floor()` del módulo `math` para obtener el techo y el piso de `num2`.
4. Imprime ambos resultados. """

# 1. Importar módulo "math".
import math

# 2. Pedimos un número decimal.
num2 = float(input("Ingrese un número decimal: "))

# 3. Calcular techo y piso del número ingresado.
techo = math.ceil(num2)
piso = math.floor(num2)

# 4. Mostrar resultados.
print(f"Techo (ceil): {techo}")
print(f"Piso (floor): {piso}")