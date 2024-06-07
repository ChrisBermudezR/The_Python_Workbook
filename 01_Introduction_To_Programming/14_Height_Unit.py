""" 
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.

Hint: One foot is 12 inches. One inch is 2.54 centimeters.

-----
Mucha gente piensa en su altura en pies y pulgadas, incluso en algunos países que 
utilizan principalmente el sistema métrico. Escriba un programa que lea una cantidad de 
pies del usuario, seguida de una cantidad de pulgadas. Una vez leídos estos valores, 
su programa debería calcular y mostrar el número equivalente de centímetros.

Pista: Un pie mide 12 pulgadas. Una pulgada son 2,54 centímetros.

"""
#Colecta de datos del usuario
pies=float(input("¿Cuál es la medida en pies?: "))
pulgadas=float(input("¿Cuál es la medida en pulgadas?: "))

#Transformación de los datos
totalpulgadas=pies*12
totalcm=(totalpulgadas*2.54) + (pulgadas*2.54)

#Imprime la respuesta
print("La medida total en cm es: {0:.2f}".format(totalcm))