def encontrar_mayor_impar (lista):
    bandera_primero = True
    for i in range(len(lista)):
        if lista[i] % 2 != 0: 
            if bandera_primero == True:
                mayor = lista[i]
                bandera_primero = False
        
            if lista[i] > mayor :
                mayor = lista[i]
        
    return mayor