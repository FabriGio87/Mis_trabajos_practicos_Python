'''2: Solicita al usuario que ingrese un valor cualquiera. Luego, muestra el valor ingresado entre backticks y el tipo de dato que corresponde al valor ingresado usando la función `type`.'''
# Solicitar un valor cualquiera
valor = input("Ingrese un valor: ")
# Mostrar el valor entre backticks y su tipo de dato
print(f"`{valor}` es de tipo {type (valor)}")