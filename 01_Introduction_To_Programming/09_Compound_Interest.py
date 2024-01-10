"""
    Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
-----
Imagine que acaba de abrir una nueva cuenta de ahorros que genera un interés del 4 por ciento anual. 
El interés que gana se paga al final del año y se agrega al saldo de la cuenta de ahorros. 
Escriba un programa que comience leyendo la cantidad de dinero depositada en la cuenta del usuario. 
Luego su programa debería calcular y mostrar el monto en la cuenta de ahorros después de 1, 2 y 3 años. 
Muestre cada cantidad de modo que se redondee a 2 decimales.

"""

montoTotal=int(input("¿Cuál es el monto inicial de la cuenta?: "))

IC01= montoTotal*((1+ 0.04)**1 - 1)
IC02= montoTotal*((1+ 0.04)**2 - 1)
IC03= montoTotal*((1+ 0.04)**3 - 1)

print("El monto total en el primer año es: $ {0:.2f}".format(montoTotal+IC01), "El segundo año el monto total sumaría: $ {0:.2f}".format(montoTotal+IC02), " y el monto total para el tercer año sería de: $ {0:.2f}".format(montoTotal+IC03))
