"""Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora, y luego muestre la paga resultante."""
# Solicitamos datos usando "float" porque podemos trabajar horas fraccionadas, así como el valor-hora puede estar dado en decimales.
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el costo por hora: "))
# Calculamos pago
pago = horas_trabajadas * valor_hora
# Mostramos el resultado
print(f"El pago total es: {pago}")
