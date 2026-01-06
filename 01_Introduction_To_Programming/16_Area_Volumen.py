"""
    Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
    Area of a circle: A = πr²
    Volume of a sphere: V = 4/3 πr³
"""
import math
print("Este programa calcula el área de un círculo y el volumen de una esfera a partir del radio proporcionado por el usuario.")
print("¿Cuál es el radio del circulo?")
r = float(input("Digite su respuesta: "))
area = math.pi * r**2
volumen = (4/3) * math.pi * r**3
print(f"El área del círculo con radio {r} es: {area:.2f}")
print(f"El volumen de la esfera con radio {r} es: {volumen:.2f}")