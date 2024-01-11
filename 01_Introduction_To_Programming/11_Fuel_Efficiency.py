"""
    In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
(MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPGto L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
-----
En Estados Unidos, la eficiencia del combustible de los vehículos normalmente se expresa en millas 
por galón (MPG). En Canadá, la eficiencia del combustible se expresa normalmente en litros por cien 
kilómetros (L/100 km). Utilice sus habilidades de investigación para determinar cómo convertir de 
MPG a L/100 km. Luego cree un programa que lea un valor del usuario en unidades americanas y muestre 
la eficiencia de combustible equivalente en unidades canadienses.
"""

galones=float(input("Escriba los galónes de gasolina a ser convertidos (MPG): "))

litrosKm= galones*253.21

print("El rendimiento en L/100km es de:\n{0:.2f}".format(litrosKm))