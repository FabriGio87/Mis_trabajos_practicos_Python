"""Escribir un programa que pida al usuario su edad y luego muestre un mensaje que le diga cuántos años le faltan para cumplir 100 años."""
# Solicitamos edad al usuario
edad = int(input("Ingrese su edad: "))
# Calculamos los años faltantes
años_faltantes = 100 - edad
# Mostramos el resultado
print(f"Te faltan {años_faltantes} años para cumplir 100 años")