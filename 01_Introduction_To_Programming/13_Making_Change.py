"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.

A one dollar coin was introduced in Canada in 1987. It is referred to as a
loonie because one side of the coin has a loon (a type of bird) on it. The two
dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
derived from the combination of the number two and the name of the loonie.


"""
#Esto se basa en que cada dólar tiene 100 centavos
nickels=5
dimes=10
quarters=25
loonies=100
toonies=200

centavos=int(input("Escriba el número de centavos: "))

print("El número de centavos devueltos por toonies es: ", centavos//toonies)
centavos=centavos%toonies

print("El número de centavos devueltos por loonies es: ", centavos//loonies)
centavos=centavos%loonies

print("El número de centavos devueltos por quarters es: ", centavos//quarters)
centavos=centavos%quarters

print("El número de centavos devueltos por dimes es: ", centavos//dimes)
centavos=centavos%dimes

print("El número de centavos devueltos por nickels es: ", centavos//nickels)
centavos=centavos%nickels

print("El número de centavos devueltos por pennies es: ", centavos)
