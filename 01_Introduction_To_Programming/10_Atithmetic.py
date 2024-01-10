"""
Create a program that reads two integers, a and b, from the user.Your program should
compute and display:
 *The sum of a and b
 *The difference when b is subtracted from a
 *The product of a and b
 *The quotient when a is divided by b
 *The remainder when a is divided by b
 *The result of log10 a
 *The result of a**b

Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.

-----
Cree un programa que lea dos números enteros, a y b, del usuario. Su programa debe
calcular y mostrar:
  *La suma de a y b
  *La diferencia cuando b se resta de a
  *El producto de a y b
  *El cociente cuando a se divide por b
  *El resto cuando a se divide por b
  *El resultado de log10 a
  *El resultado de a**b

Sugerencia: Probablemente le resulte útil la función log10 en el módulo de matemáticas.
para calcular el penúltimo elemento de la lista.

"""
import math
primerNumero=int(input("Escriba un número entero: "))
segundoNumero=int(input("Escriba otro número entero: "))

suma = primerNumero + segundoNumero
diferencia = primerNumero - segundoNumero
producto = primerNumero * segundoNumero
cociente= primerNumero / segundoNumero
residuo = primerNumero % segundoNumero
logaritmo = math.log10(primerNumero)
potencia = primerNumero**segundoNumero

print("Suma: ", suma, "Resta: ", diferencia, "Producto: ", producto, "Cociente: ", cociente, "Residuo: ", residuo, "Logaritmo: ", logaritmo, "Potencia: ", potencia)