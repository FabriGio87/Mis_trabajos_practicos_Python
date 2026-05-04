celsius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = (celsius * 1.8) + 32
print("Temperatura en °F:", fahrenheit)
print("Temperatura en °F: {}°F".format(fahrenheit))
print(f"Temperatura en °F: {fahrenheit}°F")

celsius = float(input("Ingrese la temperatura en °C: "))
print(f"Temperatura en °F: {(celsius * 1.8) + 32}°F")
