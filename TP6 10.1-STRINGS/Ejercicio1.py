'''Escribe un programa que solicite al usuario un número entero y lo convierta a un número de punto flotante. Luego, imprime el resultado.'''
# Solicito un número entero al usuario
numero_entero = int(input("Ingrese un número entero: "))
# Convierto el número solicitado a número de punto flotante
numero_float = float(numero_entero)
# Muestro el resultado
print(f"El número convertido es: {numero_float} ({type(numero_float)})")