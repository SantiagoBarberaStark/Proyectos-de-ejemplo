import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import FuncionesAuxiliares as fa
from io import open      

def crearBD():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE personas (  
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre VARCHAR(20),
                            apellido VARCHAR(20),
                            dni INTEGER UNIQUE,
                            compras INTEGER)''')

    except (sqlite3.OperationalError):
        print("Base de datos ya existente")

    else:
        print("Base de datos creada correctamente")
 
    conexion.close()


def ingresarCliente():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    n=input("Ingrese el nombre de la persona (1 Mayuscula seguido de hasta 19 minusculas)\n>>> ")
    while fa.validarTexto(n)==False:
        n=input("Ingrese el nombre de la persona (1 Mayuscula seguido de hasta 19 minusculas)\n>>> ")

    a=input("Ingrese el apellido de la persona\n>>> ")
    while fa.validarTexto(a)==False:
        n=input("Ingrese el apellido de la persona\n>>> ")

    dni=int(input("Ingrese el dni de la persona (8 enteros)\n>>> "))
    while fa.validarDni(dni)==False:
        dni=int(input("Ingrese el dni de la persona\n>>> "))

    compras=int(input("Ingrese el monto total de compras del cliente (0-1000000)\n>>> "))
    while fa.validarCompra(compras)==False:
        compras=int(input("Ingrese el monto total de compras del cliente (0-1000000)\n>>> "))

    try:
        cursor.execute("INSERT INTO personas VALUES (null,'{}','{}',{},{})".format(n,a,dni,compras))
        print("Cliente agregado con exito")

    except (sqlite3.IntegrityError):
        print("Dni ya existente")

    else:
        print("Cliente agregado con exito")

    conexion.commit()
    conexion.close()


def borrarCliente():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    doc=int(input("Ingrese el dni de la persona que desea borrar\n>>> "))

    while fa.validarDni(doc)==False:
        doc=int(input("Ingrese el dni de la persona que desea borrar\n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM personas WHERE dni={doc}")
    cliente=cursor.fetchone()
    print("Cliente:",cliente[0],cliente[1])
    opcion=int(input("Seguro que desea borrar?\n1)Para Si\n2)Para No\n>>> "))
    
    if opcion==1:
        cursor.execute(f"DELETE FROM personas WHERE dni={doc}") 
        print("Cliente borrado con exito")

    elif opcion==2:
        pass

    else:

        print("Opcion incorrecta")

    conexion.commit()
    conexion.close()


def modificarCliente():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    doc=int(input("Ingrese el dni de la persona que desea modificar\n>>> "))

    while fa.validarDni(doc)==False:
        doc=int(input("Ingrese el dni de la persona que desea borrar\n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM personas WHERE dni={doc}")
    cliente=cursor.fetchone()
    print("Cliente:",cliente[0],cliente[1])
    opcion=int(input("1)Modificar nombre\n2)Modificar apellido\n>>> "))

    if opcion==1:
        nombre=input("Ingrese el nombre nuevo\n>>> ")
        while fa.validarTexto(nombre)==False:
            nombre=input("Ingrese el nombre nuevo\n>>> ")

        cursor.execute(f"UPDATE personas SET nombre='{nombre}' WHERE dni={doc}") 
        print("Cliente modificado con exito")

    elif opcion==2:
        apellido=input("Ingrese el apellido nuevo\n>>> ")
        while fa.validarTexto(apellido)==False:
            apellido=input("Ingrese el apellido nuevo\n>>> ")

        cursor.execute(f"UPDATE personas SET apellido='{apellido}' WHERE dni={doc}") 
        print("Cliente modificado con exito")
        
    else:

        print("Opcion incorrecta")

    conexion.commit()
    conexion.close()


def consultarCliente():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    doc=int(input("Ingrese el dni de la persona que desea consultar\n>>> "))

    while fa.validarDni(doc)==False:
        doc=int(input("Ingrese el dni de la persona que desea consultar\n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM personas WHERE dni={doc}")
    cliente=cursor.fetchone()

    print("Cliente:",cliente[0],cliente[1]) 

    conexion.commit()
    conexion.close()


def verClientes():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM personas")
    usuarios=cursor.fetchall()

    print("Clientes:")
    for usuario in usuarios:
        print(usuario[1],usuario[2]," - Dni:",usuario[3])
        

def generarGrafico():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT apellido,compras FROM personas")
    usuarios=cursor.fetchall()

    datos=[]
    etiquetas=[]

    for usuario in usuarios:
        etiquetas.append(usuario[0])
        datos.append(usuario[1])

    df=pd.DataFrame(datos,etiquetas)
    plt.plot(df)
    plt.title("Compras por cliente")
    plt.xlabel("Clientes")
    plt.ylabel("Cantidad gastada[$]")
    plt.show()
    

def generarTxt():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM personas")
    usuarios=cursor.fetchall()

    fichero=open("Clientes.txt","w")
    
    for usuario in usuarios:
        
        fichero.write(usuario[1])
        fichero.write("    ")
        fichero.write(usuario[2])
        fichero.write("    ")
        fichero.write(str(usuario[3]))
        fichero.write("    ")
        fichero.write(str(usuario[4]))
        fichero.write("\n")

    fichero.close()


def reinicioDeFabrica():

    conexion=sqlite3.connect("clientes.db")
    cursor=conexion.cursor()

    opcion=int(input("Seguro que desea borrar todos los datos de la base de datos?\n1)Si\n2)No\n>>> "))

    if opcion==1:
        n=int(fa.numeroRandom())
        print("Numero generado:",n)
        num=int(input("Ingrese el numero generado para confirmar\n>>> "))
        
        if num==n:
            cursor.execute("DELETE FROM personas")
            print("Base de datos reiniciada de fabrica")
            
        else:
            print("Numero incorrecto")

    elif opcion==2:
        pass

    else:
        print("Opcion incorrecta")

    conexion.commit()
    conexion.close()    



crearBD()
print("")

print("Bienvenido al gestor de clientes")

while True:

    print("=================================")
    print("Seleccione la opcion a realizar:")
    print("")
    print("1)Ingresar cliente\n2)Borrar cliente\n3)Modificar cliente\n4)Ver clientes\n5)Consultar cliente\n6)Generar grafico de compras\n7)Generar txt con los clientes\n8)Reiniciar base de datos de fabrica\n9)Salir del sistema")
    opcion=int(input(">>> "))
    print("")
    fa.limpiarPantalla()

    if opcion==1:

        ingresarCliente()

    elif opcion==2:

        borrarCliente()

    elif opcion==3:

        modificarCliente()

    elif opcion==4:

        verClientes()

    elif opcion==5:

        consultarCliente()

    elif opcion==6:

        generarGrafico()

    elif opcion==7:

        generarTxt()

    elif opcion==8:

        reinicioDeFabrica()
    
    elif opcion==9:

        break

    else:

        print("Opcion incorrecta")
