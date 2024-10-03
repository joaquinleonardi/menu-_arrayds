from package_arrays.validate import *

def get_int (mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos=None) -> None|int:

    numero = int(input(mensaje))
    numero = validate_number(numero,minimo,maximo,mensaje_error,reintentos)
    
    return numero



mensaje = "ingrese un numero entre el 5 y el 10: "
mensaje_error = "error, ingrese un numero valido: "
mensaje_2 = "ingrese numero del 2.2 al 5.5: "
reintentos = 2


#print(get_int(mensaje,mensaje_error,5,10,reintentos))

#############################################

def get_float(mensaje_2,mensaje_error,minimo,maximo,reintentos):

    numero = float(input(mensaje_2))
    numero = validate_number(numero,minimo,maximo,mensaje_error,reintentos)
    
    return numero


#print(get_float(mensaje_2,mensaje_error,2.2,5.5,reintentos))


#############################################

def get_string(minimo,maximo,reintentos):
    texto = str(input("ingrese un texto que tenga entre 4 y 10 caracteres "))
    texto = validate_length(texto,minimo,maximo,reintentos)
    return texto

#print (get_string(4,10,reintentos))


#################################################
