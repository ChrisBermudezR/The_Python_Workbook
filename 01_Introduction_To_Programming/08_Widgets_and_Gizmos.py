"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
-----
Un minorista online vende dos productos: aditamentos y artilugios. Cada aditamentos pesa 75gramos.
Cada artilugio pesa 112 gramos. Escribe un programa que lea el número de aditamentos y el 
número de artilugios en un pedido del usuario. A continuación, su programa debe calcular 
y mostrar el peso total del pedido.

"""
widgets=int(input("¿Cuántos widgets solicitó el cliente?: "))
gizmos=int(input("¿Cuántos gizmos solicitó el cliente?:"))

pesoTotal=widgets*75+gizmos*112

print(f"El peso total del pedido es: {pesoTotal} gr.")