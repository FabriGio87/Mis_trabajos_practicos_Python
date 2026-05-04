"""Ejercicio 2: Uso de if, elif y else 1. Escribe un programa que solicite al usuario ingresar una calificación (de 0 a 100). 2. Si la calificación es mayor o igual a 90, imprime "A". 3. Si la calificación está entre 80 y 89, imprime "B". 4. Si la calificación está entre 70 y 79, imprime "C". 5. Si la calificación está por debajo de 70, imprime "F"."""

# 1. Pedir calificación
nota = int(input("Ingrese una calificación (0-100): "))

# 2-5. Evaluar con if, elif, else
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")