"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1)/2

Escriba un programa que lea un número entero positivo, n, del usuario y luego muestre 
la suma de todos los números enteros de 1 a n. La suma de los primeros n números enteros 
positivos se puede calcular de la siguiente manera utilizando la fórmula:

sum = (n)(n + 1)/2

"""
numero=int(input("Intriduzca un número entero para devolver la suma de todos los números anteriore: "))

suma = numero*(numero + 1)/2

print(f"La suma de los números dió como resultado: {int(suma)}")