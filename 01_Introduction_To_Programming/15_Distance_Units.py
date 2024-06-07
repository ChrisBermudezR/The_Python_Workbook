"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.

---



"""

measurement=float(input("¿Cuál es el valor de su medida en pies?: "))

pulgadas=measurement*12
yardas=measurement*0.33
millas=measurement*0.00018939

print(f"La medida en pulgadas es {pulgadas}, en yardas es {yardas} y en millas en {millas}")