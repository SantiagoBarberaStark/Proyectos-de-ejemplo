import os
import re

def limpiarPantalla():

    os.system("cls")

def validarNombreApellido(texto):

    if not re.match(r"^[A-Z][a-z]{0,29}$",texto):
                            
        print("Nombre invalido")
        return False

    else:

        return True
    
def validarDni(dni):

    if dni<10000000 or dni>99999999:
                            
        print("Dni invalido")
        return False

    else:

        return True
    
def validarMatricula(matricula):

    if matricula<10000 or matricula>99999:
                            
        print("Matricula invalida")
        return False

    else:

        return True
    
def validarNumeroVuelo(numero):

    if numero<1000 or numero>9999:
                            
        print("Numero invalido")
        return False

    else:

        return True

def validarAsientosVuelo(numero):

    if numero<200 or numero>800:
                            
        print("Cantidad de asientos invalida")
        return False

    else:

        return True
    
