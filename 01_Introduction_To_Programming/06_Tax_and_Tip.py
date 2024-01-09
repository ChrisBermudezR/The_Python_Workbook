"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
-----
El programa que cree para este ejercicio comenzará leyendo el coste de una comida pedida 
en un restaurante por el usuario. A continuación, el programa calculará los impuestos y propina de la comida. 
Utilice el tipo impositivo local para calcular la cantidad de impuestos a pagar.
Calcule la propina como el 18% del importe de la comida (sin impuestos). 
La salida de programa debe incluir el importe del impuesto, el importe de la propina y el total 
general de la comida, incluidos el impuesto y la propina.
Formatee la salida para que todos los valores se muestren con dos decimales.

"""
totalcost=float(input("¿Cuál es el costo de de la comida?: "))
impuestos=totalcost*0.18
propina=totalcost*0.1

print("el valor total de la comida es: $ {0:.2f} ".format(totalcost), ". Los impuestos son: $ {0:.2f} ".format(impuestos), "y la propina total es: $ {0:.2f}".format(propina), ". El total a pagar es: ${0:.2f}".format(totalcost + impuestos +propina))
