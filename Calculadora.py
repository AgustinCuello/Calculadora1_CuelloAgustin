
from Biblioteca import *

A=0
B=0
suma=0
resta=0
multiplicacion=0
divicion=0
factoreo=0
opc=0

#Menú
def menu():
    print("1. Introducir primer valor:")
    print("A = ",A)
    print("2. Introducir segundo valor:")
    print("B = ",B)
    print("3. Calcular:")
    print("4. Mostrar resultados:")
    print("5. Salir:")
    print("\n")
	
#Opciones
def opciones(opc=0):
    opcion = int(input("Selecione una Opción... "))
    if opcion >=6 or opcion<=0:
        print("Error: No existe tal opcion. Intentelo de nuevo")
    return opcion


#Programa
while opc!=5:
    
    #Lamar al menú
    menuPrincipal = menu()
    opc = opciones()
    
    #Confirmar que los valores A & B se cargaron
    Primero=False
    Segundo=False
    
    #Introduciendo A
    if(opc == 1):
        A=valores()
    
    #Introduciendo B
    if(opc == 2):
        B=valores()
    
    #Confirmar si el divisor es 0
    EsCero=False
    
    #Confirmar si los calculos se realizaron
    CalculosHechos=False
    
    #Hacer los calculos
    if(opc == 3):
        suma=sumar(A,B)
        resta=restar(A,B)
        if B!=0:
            divicion=dividir(A,B)
        else:
            EsCero=True
        multiplicacion=multiplicar(A,B)
        factoreo=factorial(A,B)
        
    #Mostrar resultados
    if(opc == 4):
        if CalculosHechos and Primero and Segundo:
            print("El resultado de ",A,"+",B,"es ",suma)
            print("El resultado de ",A,"-",B,"es ",resta)
            print("El resultado de ",A,"x",B,"es ",multiplicacion)
            if EsCero:
                print("No se puede dividir por 0")
            else:
                print("El resultado de ",A,"/",B,"es ",)
            print("El resultado de ",A,"! es ",factoreo)
        else:
            print("Error: Revise los datos y calcule")
               
            
        
        
        
