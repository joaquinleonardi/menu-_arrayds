#from input import * 

def validate_number(numero,minimo,maximo,mensaje_error,reintentos):
    
    contador_de_intentos = 0
    while numero < minimo or numero > maximo:

        if contador_de_intentos == reintentos:
            return None
        
        if type(numero) == int:
            numero = int (input(mensaje_error))
        elif type (numero) == float:
            numero = float (input(mensaje_error))
        contador_de_intentos += 1
        
    return numero


################################################

def validate_length (texto,minimo,maximo,reintentos):
    contador_intentos = 0
    for i in range (len(texto)):
        pass
    i = i + 1
    while i < minimo or i > maximo:

        if contador_intentos == reintentos :
            return None
        contador_intentos += 1 
        texto = str(input("error, ingerse texto valido "))
        for i in range (len(texto)):
            pass
        i = i + 1
    return texto