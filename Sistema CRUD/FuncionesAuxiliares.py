import re
import os
import random

def validarDni(dni):

    if dni<11111111 or dni>99999999:

        print("Dni fuera de formato (8 enteros)")
        return False

    else:

        return True


def validarCompra(n):

    if n<0 or n>1000000:

        print("Gasto fuera de rango (0-1000000)")
        return False

    else:

        return True


def validarTexto(t):

    if not re.match('[A-Z]{1}[a-z]{2,17}$',t): 

        print("Nombre o apellido fuera de formato (1 Mayuscula seguido de hasta 20 minusculas)")
        return False

    else:

        return True


def limpiarPantalla():

    os.system("cls")
    

def numeroRandom():

    return random.randint(1111,9999)