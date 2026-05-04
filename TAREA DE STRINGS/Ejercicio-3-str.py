""" Ejercicio 3: Modificación y acceso por rangos
1. Declara una variable `var3` usando triple comillas simples (`'''`) con varias líneas de texto.
2. Extrae una porción de la cadena desde el inicio hasta el quinto carácter.
3. Extrae una porción desde el décimo hasta el final."""
# Creamos una cadena multilínea con comillas simples
var3 = '''Python es un lenguaje muy versátil y potente ideal para aprender programación'''
# Desde el inicio hasta el quinto carácter
inicio = var3[:5]
# Desde el décimo carácter hasta el final
final = var3[10:]
# Mostrar resultados
print(f"Primeros 5 caracteres: {inicio}")
print(f"Desde el carácter 10 en adelante: {final}")