
presion = float(input("Ingrese la presion (en Pascale): "))
volumen = float(input("Ingrese el volumen (en litros): "))
temperatura = float(input("Ingrese la temperatura (en °C): "))

moles = presion*volumen/8.314*(temperatura+273.15)


print("El número de moles es:", moles)