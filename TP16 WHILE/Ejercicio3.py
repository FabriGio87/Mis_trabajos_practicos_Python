"""### Ejercicio 3: Uso de `while` con `continue`
1. Escribe un programa que solicite al usuario ingresar números.
2. Si el número es negativo, utiliza `continue` para saltar a la siguiente iteración sin imprimir el número.
3. Si el número es positivo o cero, imprímelo en la pantalla."""

while True:
    numero = int(input("Ingresá un número : "))

    if numero < 0:
        continue  # salta todo lo que sigue y vuelve al inicio del while

    print(f"Número válido: {numero}")