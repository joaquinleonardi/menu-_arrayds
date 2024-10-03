from package_arrays.input import *


def pedir_numeros ():
    lista = [0] * 10
    
    for i in range (len(lista)):
        resultado = get_int("un numero entre el -1000 y 1000 ","error reingrese numero ",-1000,1000)
        lista[i] = resultado
    return lista 

#lista = pedir_numeros()

def identificar_positivos (lista):
    positivos = 0
    negativos = 0
    for i in range (len(lista)):
        if lista[i] > 0 :
            positivos += 1
        elif lista[i] < 0:
            negativos += 1
    print (f"cantidad de numeros negativos encontrados {negativos} \ncantidad de positivos encontrados {positivos}")

#identificar_positivos (lista)


def sumatoria_pares (lista):
    acumulador_pares = 0
    acumulador_impares = 0
    for i in range (len(lista)):
        if lista[i] % 2 == 0:
            acumulador_pares += lista[i]
    print (f"la suma de los pares es {acumulador_pares}")
        

#sumatoria_pares(lista)

#def encontrar_mayor_impar (lista):
#    bandera_primero = True
#    for i in range(len(lista)):
#        if bandera_primero == True:
#            mayor = lista[i]
#            bandera_primero = False
#        
#        if lista[i] > mayor :
#            mayor = lista[i]
#    print (f"el numero impar mas grande es el {mayor}")


#encontrar_mayor_impar (lista)



def mostrar_lista(lista):
    print (lista)


#mostrar_lista(lista)



def listar_pares (lista):
    listar_pares = []
    for i in range(len(lista)):

        if lista[i] % 2 == 0:
            listar_pares += str(lista[i])
    print (listar_pares)
    


#listar_pares (lista)


def listar_impares(lista):
    posicion_impares = []
    for i in range (len(lista)):
        if lista[i] % 2 != 0:
            posicion_impares += str(i)
    print (posicion_impares)


#listar_impares(lista)