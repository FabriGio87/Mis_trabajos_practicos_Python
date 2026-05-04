"""### Ejercicio 2: Uso de `while` con `break`
1. Escribe un programa que solicite al usuario ingresar números.
2. Si el usuario ingresa el número 0, el programa debe detenerse usando `break`.
3. Si el número ingresado no es 0, imprímelo en la pantalla."""

while True:
    numero = int(input("Ingrese un número: (0 para salir)"))
    if numero == 0:
        print("Programa finalizado")
        break

    print("Ingresaste: ", numero)
