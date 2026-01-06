""" 
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""

print("Este programa calcula el volumen de un cilindro.")
radius = float(input("Ingrese el radio del cilindro: "))
height = float(input("Ingrese la altura del cilindro: "))

volume = 3.14159 * radius**2 * height

print(f"El volumen del cilindro es {volume:.1f} unidades cúbicas.")