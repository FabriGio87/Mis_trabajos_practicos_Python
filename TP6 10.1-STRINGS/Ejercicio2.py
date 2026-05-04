'''Crea un programa que tome dos números enteros ingresados por el usuario y realice las siguientes operaciones: suma, resta, multiplicación y división. Imprime los resultados.'''
#Vamos a solicitar dos números enteros.
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))
#Operaciones matemáticas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
#En division tengo que aprender cómo NO dividir por 0
division = numero1 / numero2 
print(f"SUMA: {suma}")
print(f"RESTA: {resta}")
print(f"MULTIPLICACIóN: {multiplicacion}")
print(f"DIVISIÓN: {division}")