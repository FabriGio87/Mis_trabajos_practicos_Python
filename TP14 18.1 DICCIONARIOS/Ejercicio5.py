"""### Ejercicio 5: Lista de vehiculos
Codigo base: 
vehiculos = [{'marca': 'Ford','modelo': 'Mustang','año': 1964,'precio': {'pesos': 5000, 'dolares': 600000}},{'marca': 'Toyota','modelo': 'Corolla','año': 2020,'precio': {'pesos': 3500, 'dolares': 18000}},{'marca': 'Renault','modelo': 'Clio','año': 2015,'precio': {'pesos': 2800, 'dolares': 12000}}]
# Validar si el precio en dólares supera cierto umbral
umbral = 20000 for auto in vehiculos: if auto['precio']['dolares'] > umbral: print(f"{auto['modelo']} supera el umbral de precio.")
else:print(f"{auto['modelo']} está dentro del rango accesible.")
Consignas. Ejecutá el código y observá qué modelos superan el umbral de precio.Cambiá el valor del umbral a 15000 y analizá cómo cambia la salida.Agregá un nuevo vehículo a la lista con datos inventados.Mostrá solo los modelos fabricados después del año 2018."""

vehiculos = [{'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964,'precio': {'pesos': 5000, 'dolares': 600000}},{'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2020, 'precio': {'pesos': 3500, 'dolares': 18000}},{'marca': 'Renault', 'modelo': 'Clio', 'año': 2015, 'precio': {'pesos': 2800, 'dolares': 12000}}]

# 🔹 1. Umbral inicial
umbral = 20000

print("-Evaluación con umbral 20000-")
for auto in vehiculos:
    if auto['precio']['dolares'] > umbral:
        print(f"{auto['modelo']} supera el umbral de precio.")
    else:
        print(f"{auto['modelo']} está dentro del rango accesible.")

# 🔹 2. Cambiar umbral a 15000
umbral = 15000

print("\n-Evaluación con umbral 15000-")
for auto in vehiculos:
    if auto['precio']['dolares'] > umbral:
        print(f"{auto['modelo']} supera el umbral de precio.")
    else:
        print(f"{auto['modelo']} está dentro del rango accesible.")

# 🔹 3. Agregar nuevo vehículo
nuevo_auto = {'marca': 'Chevrolet','modelo': 'Onix','año': 2022,'precio': {'pesos': 4000, 'dolares': 17000}}

vehiculos.append(nuevo_auto)

# 🔹 4. Mostrar modelos después de 2018
print("\n-Vehículos posteriores a 2018-")
for auto in vehiculos:
    if auto['año'] > 2018:
        print(auto['modelo'])