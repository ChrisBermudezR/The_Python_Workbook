"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
-----
En muchas jurisdicciones se añade un pequeño depósito a los envases de bebidas para animar a 
la gente a reciclarlos. a reciclarlos. En una jurisdicción concreta, los envases de 
bebidas de un litro o menos tienen un depósito de 0,10 litro o menos tienen un depósito
de 0,10 dólares, y los de más de un litro tienen un depósito de 0,25 dólares. 0,25 $ de depósito.
Escribe un programa que lea el número de envases de cada tamaño del usuario. Su programa 
debe continuar calculando y mostrando el reembolso que se recibirá por devolver esos envases.
Formatee la salida de modo que incluya un signo y muestre siempre exactamente dos decimales.

"""

lessLiterContainer=float(input("Enter the number of container smaller than a liter to be deposit: "))
containeLiterPlus=float(input("Enter the number of containers bigger than a liter  to be deposit: "))

totallessLiterContainer=lessLiterContainer*0.1
totalcontaineLiterPlus=containeLiterPlus*0.25
print("The amount of money returned is $ {0:.2f} USD".format(totallessLiterContainer + totalcontaineLiterPlus))