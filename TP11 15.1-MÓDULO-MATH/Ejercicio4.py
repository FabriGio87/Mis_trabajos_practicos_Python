"""Ejercicio 4: Uso de `isnan()`
1. Usa `import math` para importar el módulo de matemáticas.
2. Declara una variable `num3` que contenga un valor de tipo `float('nan')`.
3. Usa la función `math.isnan()` para verificar si `num3` es `NaN` (Not a Number).
4. Imprime un mensaje indicando si el valor es `NaN` o no."""

# 1. Importar módulo
import math

# 2. Declarar variable con NaN
num3 = float('nan')

# 3. Verificar si es NaN
es_nan = math.isnan(num3)

# 4. Mostrar resultado
if es_nan:print("El valor es NaN")
else:print("El valor NO es NaN")

print("Es NaN" if math.isnan(num3) else "No es NaN")