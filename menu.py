from package_arrays.array_generales import *
from package_arrays.especificas import *
#from package_arrays.input import *
from os import system

bandera_primer_paso = False
bandera = True
while bandera:

    print("1-Pedir el ingreso de 10 números enteros entre -1000 y 1000 \n 2-Mostrar la cantidad de números positivos y negativos \n 3-mostrar la sumatoria de los números pares \n 4-informar el mayor de los números impares \n 5-listar todos los números ingresados \n 6-listar todos los números pares \n 7-listar los números de las posiciones impares \n 8-salir")
    print ("")
    opcion = input("ingrese una opcion: ")
    
    
    error = "sin acceso hasta tener la opcion 1 completa"

    match opcion:
        case "1":
            bandera_primer_paso = True
            lista = pedir_numeros ()
            print(lista)
            
        case "2":
            if bandera_primer_paso == False:
                print (error)
            else:
                identificar_positivos (lista)
        case "3":
            if bandera_primer_paso == False:
                print (error)
            else:
                sumatoria_pares(lista)
        case "4":
            if bandera_primer_paso == False:
                print (error)
            else:
                mayor = encontrar_mayor_impar (lista)
                print (f"el numero impar mas grande es el {mayor}")
        case "5":
            if bandera_primer_paso == False:
                print (error)
            else:
                mostrar_lista(lista)
        case "6":
            if bandera_primer_paso == False:
                print (error)
            else:
                listar_pares (lista)
        case "7":
            if bandera_primer_paso == False:
                print (error)
            else:
                listar_impares(lista)
        case "8":
            print("")
            print ("saliendo del programa ")
            break
        
    system("pause")
    system ("csl")
