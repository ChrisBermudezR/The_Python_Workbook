"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2 . You can use the formula vf =
√v2i + 2ad to compute the final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known  
"""
import math

altura = float(input("¿Cuál es la altura (en metros) desde la que se deja caer el objeto?: "))

Vf = math.sqrt(0 + 2 * 9.81 * altura)

print(f"La velocidad final del objeto al llegar al suelo es de {Vf:.2f} m/s.")