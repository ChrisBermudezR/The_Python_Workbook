"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

Hint: There are 43,560 square feet in an acre.
-----
Cree un programa que lea del usuario la longitud y anchura del campo de un agricultor en pies. Muestre el área del campo en acres.

Sugerencia: Hay 43,560 pies cuadrados en un acre.

"""

length=float(input("What are the length, in feet units, of the field?: "))
width=float(input("What are the width, in feet units, of the field?: "))

area=(length*width)*0.000022957

print(f"You field area in acres is: {area}")


