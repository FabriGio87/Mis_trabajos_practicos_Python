"""Ejercicio 3: Uso de `pow()` y `sqrt()`
1. Usa `import math` para importar el módulo de matemáticas.
2. Declara dos variables `base` y `exponente`.
3. Usa la función `pow()` para elevar `base` a la potencia `exponente` y almacena el resultado.
4. Usa `sqrt()` para obtener la raíz cuadrada del resultado de la potencia.
5. Imprime ambos resultados."""

# 1. Importamos módulo "math".
import math

# 2. Declaramos las variables.
base = 9
exponente = 3

# 3. Potencia.
potencia = math.pow(base, exponente)

# 4. Raíz cuadrada.
raiz = math.sqrt(potencia)

# 5. Imprimimos resultados.
print(f"Potencia: {potencia}")
print(f"Raíz cuadrada: {raiz}")