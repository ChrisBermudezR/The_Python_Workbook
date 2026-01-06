""" 
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:

q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change

for water. The specific heat capacity of water is 4.186 J/g°C.  

Extend your program so that it also computes the cost of heating the water. Elec-
tricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.


"""

C = 4.186 #J/g°C
T = float(input("Cual es la temperatura que desea aumentar? "))
m = float(input("Cual es la masa de agua en gramos? "))

q = m * C * T

print(f"La cantidad de energia necesaria es de {q} Joules")

#Calculo del costo
kWh = q / 3600000 #Conversion de Joules a kWh
cost_per_kWh = 8.9 / 100 #Costo en dolares por kWh
total_cost = kWh * cost_per_kWh 
print(f"El costo total de calentar el agua es de ${total_cost:.4f} dolares.")