import math

#Introducir valores
def valores(valor:int):
	valor = int(input("Valor: "))
	return (valor)

#Sumar A & B
def sumar(valor1:int,valor2:int):
	return sum(valor1,valor2)

#Restar A & B
def restar(valor1:int,valor2:int):
	return valor1 - valor2

#Multiplicar A & B
def multiplicar(valor1:int,valor2:int):
	return valor1 * valor2 

#Dividir A & B
def dividir(valor1:int,valor2:int)->float:
    return valor1/valor2

#Factorial de A
def factorial(valor1:int):
    return math.factorial(valor1)

