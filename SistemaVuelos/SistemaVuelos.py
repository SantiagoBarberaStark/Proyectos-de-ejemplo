import sqlite3
import FuncionesAuxiliares as fa

def crearBD():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    try:

        cursor.execute('''CREATE TABLE pasajeros (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre VARCHAR(30) NOT NULL,
                            apellido VARCHAR(30) NOT NULL,
                            dni INTEGER UNIQUE NOT NULL)''')
        
        cursor.execute('''CREATE TABLE piloto (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre VARCHAR(30) NOT NULL,
                            apellido VARCHAR(30) NOT NULL,
                            matricula INTEGER UNIQUE NOT NULL)''')
        
        cursor.execute('''CREATE TABLE vuelo (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            numero INTEGER UNIQUE NOT NULL,
                            asientosTotales INTEGER NOT NULL,
                            piloto_id INTEGER NOT NULL,
                            FOREIGN KEY(piloto_id) REFERENCES piloto(id))''')
        
        cursor.execute('''CREATE TABLE pasajeros_vuelo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vuelo_id INTEGER,
                    pasajero_id INTEGER,
                    FOREIGN KEY(vuelo_id) REFERENCES vuelo(id),
                    FOREIGN KEY(pasajero_id) REFERENCES pasajeros(id))''')
        
    except (sqlite3.OperationalError):

        print("Bases de datos ya existentes")
        print("")

    else:

        print("Bases de datos abiertas con exito")
        print("")

    conexion.close()

def borrarBD():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    opcion=int(input("Seguro que desea borrar todos los datos de la base de datos?\n1)Si\n2)No\n>>> "))

    if opcion==1:
        
        cursor.execute("DELETE FROM pasajeros")
        cursor.execute("DELETE FROM vuelo")
        cursor.execute("DELETE FROM piloto")
        print("Base de datos borrada con exito")
            
    elif opcion==2:

        pass

    else:

        print("Opcion incorrecta")

    conexion.commit()
    conexion.close()   

#--------------------------------------------PASAJERO--------------------------------------------

def ingresarPasajero():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    nombre=input("Ingrese el nombre del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
    while not fa.validarNombreApellido(nombre):
        nombre=input("Ingrese el nombre del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

    apellido=input("Ingrese el apellido del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
    while not fa.validarNombreApellido(apellido):
        nombre=input("Ingrese el apellido del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

    dni=int(input("Ingrese el dni del pasajero (8 enteros): \n>>> "))
    while not fa.validarDni(dni):
        dni=int(input("Ingrese el dni del pasajero (8 enteros): \n>>> "))

    try:

        cursor.execute("INSERT INTO pasajeros VALUES (null,'{}','{}','{}')".format(nombre,apellido,dni))

    except (sqlite3.IntegrityError):

        print("Dni ya existente")

    else:

        print("Pasajero agregado con exito")

    conexion.commit()
    conexion.close()

def borrarPasajero():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    dni=int(input("Ingrese el dni del pasajero que desea borrar (8 enteros): \n>>> "))
    while not fa.validarDni(dni):
        dni=int(input("Ingrese el dni del pasajero que desea borrar (8 enteros): \n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM pasajeros WHERE dni={dni}")
    pasajero=cursor.fetchone()

    if pasajero is not None:

        print("Pasajero:",pasajero[0],pasajero[1])

        opcion=int(input("Seguro que desea borrar al pasajero?\n1)Para Si\n2)Para No\n>>>"))

        if opcion==1:

            cursor.execute(f"DELETE FROM pasajeros WHERE dni={dni}")
            print("Pasajero borrado con exito")

        elif opcion==2:

            pass

        else:

            print("Opcion incorrecta")

    else:

        print("No se encontro ningun pasajero con ese Dni")

    conexion.commit()
    conexion.close()

def modificarPasajero():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    dni=int(input("Ingrese el dni del pasajero que desea modificar(8 enteros): \n>>> "))
    while not fa.validarDni(dni):
        dni=int(input("Ingrese el dni del pasajero que desea modificar(8 enteros): \n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM pasajeros WHERE dni={dni}")
    pasajero=cursor.fetchone()

    if pasajero is not None:

        print("Pasajero:",pasajero[0],pasajero[1])

        opcion=int(input("1)Modificar nombre\n2)Modificar apellido\n>>> "))

        if opcion==1:

            nombre=input("Ingrese el nombre nuevo del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
            while not fa.validarNombreApellido(nombre):
                nombre=input("Ingrese el nombre nuevo del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

            cursor.execute(f"UPDATE pasajeros SET nombre='{nombre}' WHERE dni={dni}") 
            print("Pasajero modificado con exito")

        elif opcion==2:

            apellido=input("Ingrese el apellido nuevo del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
            while not fa.validarNombreApellido(apellido):
                nombre=input("Ingrese el apellido nuevo del pasajero (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

            cursor.execute(f"UPDATE pasajeros SET apellido='{apellido}' WHERE dni={dni}") 
            print("Cliente modificado con exito")

        else:

            print("Opcion incorrecta")
    
    else:

        print("No se encontro ningun pasajero con ese Dni")

    conexion.commit()
    conexion.close()

def consultarPasajero():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    dni=int(input("Ingrese el dni del pasajero que desea consultar(8 enteros): \n>>> "))
    while not fa.validarDni(dni):
        dni=int(input("Ingrese el dni del pasajero que desea consultar(8 enteros): \n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM pasajeros WHERE dni={dni}")
    pasajero=cursor.fetchone()

    if pasajero is not None:

        print("Pasajero:",pasajero[0],pasajero[1])

    else:

        print("No se encontro ningun pasajero con ese Dni")

    conexion.commit()
    conexion.close()

def verPasajeros():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM pasajeros")
    pasajeros=cursor.fetchall()

    if len(pasajeros)>0:

        print("Pasajeros:")

        for pasajero in pasajeros:
            print(pasajero[1],pasajero[2]," - Dni:",pasajero[3])

    else:

        print("No hay pasajeros registrados")

#--------------------------------------------PILOTO--------------------------------------------

def ingresarPiloto():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    nombre=input("Ingrese el nombre del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
    while not fa.validarNombreApellido(nombre):
        nombre=input("Ingrese el nombre del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

    apellido=input("Ingrese el apellido del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
    while not fa.validarNombreApellido(apellido):
        apellido=input("Ingrese el apellido del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

    matricula=int(input("Ingrese la matricula del piloto (5 enteros): \n>>> "))
    while not fa.validarMatricula(matricula):
        matricula=int(input("Ingrese la matricula del piloto (5 enteros): \n>>> "))

    try:

        cursor.execute("INSERT INTO piloto VALUES (null,'{}','{}','{}')".format(nombre,apellido,matricula))

    except (sqlite3.IntegrityError):

        print("Matricula ya existente")

    else:

        print("Piloto agregado con exito")

    conexion.commit()
    conexion.close()

def borrarPiloto():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    matricula=int(input("Ingrese la matricula del piloto que desea borrar(5 enteros): \n>>> "))
    while not fa.validarMatricula(matricula):
        matricula=int(input("Ingrese la matricula del piloto que desea borrar(5 enteros): \n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM piloto WHERE matricula={matricula}")
    piloto=cursor.fetchone()

    if piloto is not None:

        print("Piloto:",piloto[0],piloto[1])

        opcion=int(input("Seguro que desea borrar al piloto?\n1)Para Si\n2)Para No\n>>>"))

        if opcion==1:

            cursor.execute(f"DELETE FROM pilotos WHERE matricula={matricula}")
            print("Piloto borrado con exito")

        elif opcion==2:

            pass

        else:

            print("Opcion incorrecta")

    else:

        print("No se encontro ningun piloto con esa matricula")

    conexion.commit()
    conexion.close()

def modificarPiloto():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    matricula=int(input("Ingrese la matricula del piloto que desea modificar (5 enteros): \n>>> "))
    while not fa.validarMatricula(matricula):
        matricula=int(input("Ingrese la matricula del piloto que desea modificar(5 enteros): \n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM piloto WHERE matricula={matricula}")
    piloto=cursor.fetchone()

    if piloto is not None:

        print("Piloto:",piloto[0],piloto[1])

        opcion=int(input("1)Modificar nombre\n2)Modificar apellido\n>>> "))

        if opcion==1:

            nombre=input("Ingrese el nombre nuevo del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
            while not fa.validarNombreApellido(nombre):
                nombre=input("Ingrese el nombre nuevo del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

            cursor.execute(f"UPDATE pilotos SET nombre='{nombre}' WHERE matricula={matricula}") 
            print("Piloto modificado con exito")

        elif opcion==2:

            apellido=input("Ingrese el apellido nuevo del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")
            while not fa.validarNombreApellido(apellido):
                apellido=input("Ingrese el apellido nuevo del piloto (1 Mayuscula seguida de hasta 29 minusculas): \n>>> ")

            cursor.execute(f"UPDATE pilotos SET apellido='{apellido}' WHERE matricula={matricula}") 
            print("Piloto modificado con exito")

        else:

            print("Opcion incorrecta")

    else:

        print("No se encontro ningun piloto con esa matricula")

    conexion.commit()
    conexion.close()

def consultarPiloto():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    matricula=int(input("Ingrese la matricula del piloto que desea consultar(5 enteros): \n>>> "))
    while not fa.validarMatricula(matricula):
        matricula=int(input("Ingrese la matricula del piloto que desea consultar(5 enteros): \n>>> "))

    cursor.execute(f"SELECT nombre,apellido FROM piloto WHERE matricula={matricula}")
    piloto=cursor.fetchone()

    if piloto is not None:

        print("Piloto:",piloto[0],piloto[1])

    else:

        print("No se encontro ningun piloto con esa matricula")

    conexion.commit()
    conexion.close()

def verPilotos():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM piloto")
    pilotos=cursor.fetchall()

    if len(pilotos)>0:

        print("Pilotos:")

        for piloto in pilotos:
            print(piloto[1],piloto[2]," - Matricula:",piloto[3])

    else:

        print("No hay pilotos registrados")

#--------------------------------------------VUELOS--------------------------------------------

def ingresarVuelo():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    numero=int(input("Ingrese el numero del vuelo (4 enteros): \n>>> "))
    while not fa.validarNumeroVuelo(numero):
        numero=int(input("Ingrese el numero del vuelo (4 enteros): \n>>> "))

    asientosTotales=int(input("Ingrese la cantidad de asientos del vuelo (200 a 800): \n>>> "))
    while not fa.validarAsientosVuelo(asientosTotales):
        asientosTotales=int(input("Ingrese la cantidad de asientos del vuelo (200 a 800): \n>>> "))

    pilotoID=int(input("Ingrese el id del piloto a asignar este vuelo: \n>>> "))

    try:

        cursor.execute(f"SELECT nombre,apellido FROM piloto WHERE id={pilotoID}")
        piloto=cursor.fetchone()

        if piloto is None:

            print("Piloto inexistente")

        else:

            cursor.execute("INSERT INTO vuelo VALUES (null,'{}','{}','{}')".format(numero,asientosTotales,pilotoID))
            print("Vuelo agregado con exito")

    except (sqlite3.IntegrityError):

        print("Numero de vuelo ya existente")

    conexion.commit()
    conexion.close()

def borrarVuelo():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    numero=int(input("Ingrese el numero del vuelo a borrar (4 enteros): \n>>> "))
    while not fa.validarNumeroVuelo(numero):
        numero=int(input("Ingrese el numero del vuelo a borrar(4 enteros): \n>>> "))

    cursor.execute(f"SELECT numero,asientosTotales FROM vuelo WHERE numero={numero}")
    vuelo=cursor.fetchone()

    if vuelo is not None:

        print("Vuelo:",vuelo[0])

        opcion=int(input("Seguro que desea borrar el vuelo?\n1)Para Si\n2)Para No\n>>>"))

        if opcion==1:

            cursor.execute(f"DELETE FROM vuelo WHERE numero={numero}")
            print("Vuelo borrado con exito")

        elif opcion==2:

            pass

        else:

            print("Opcion incorrecta")

    else:

        print("No se encontro ningun vuelo con ese numero")

    conexion.commit()
    conexion.close()

def modificarVuelo():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    numero=int(input("Ingrese el numero del vuelo a modificar(4 enteros): \n>>> "))
    while not fa.validarNumeroVuelo(numero):
        numero=int(input("Ingrese el numero del vuelo a modificar(4 enteros): \n>>> "))

    cursor.execute(f"SELECT numero,asientosTotales FROM vuelo WHERE numero={numero}")
    vuelo=cursor.fetchone()

    if vuelo is not None:

        print("Vuelo:", vuelo[0])

        opcion=int(input("1)Modificar piloto\n2)Modificar cantidad de asientos\n>>> "))

        if opcion==1:

            piloto=int(input("Ingrese el id del piloto nuevo\n>>> "))

            try:

                cursor.execute(f"SELECT nombre,apellido FROM piloto WHERE id={piloto}")
                piloto=cursor.fetchone()

                if piloto is not None:

                    cursor.execute(f"UPDATE vuelo SET piloto_id='{piloto}' WHERE numero={numero}") 
                    print("Vuelo modificado con exito")

            except:

                    print("Piloto inexistente")

        elif opcion==2:

            cantAsientos=int(input("Ingrese la cantidad de asientos nueva\n>>> "))

            cursor.execute(f"UPDATE piloto SET cantidadAsientos='{cantAsientos}' WHERE numero={numero}") 
            print("Vuelo modificado con exito")

        else:

            print("Opcion incorrecta")

    else:

        print("No se encontro ningun vuelo con ese numero")

    conexion.commit()
    conexion.close()

def consultarVuelo():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    numero=int(input("Ingrese el numero del vuelo a consultar (4 enteros): \n>>> "))
    while not fa.validarNumeroVuelo(numero):
        numero=int(input("Ingrese el numero del vuelo a consultar(4 enteros): \n>>> "))

    cursor.execute(f"SELECT numero,piloto_id,asientosTotales FROM vuelo WHERE numero={numero}")
    vuelo=cursor.fetchone()

    cursor.execute(f"SELECT matricula FROM piloto WHERE id={vuelo[1]}")
    piloto=cursor.fetchone()

    if vuelo is not None:

        print("Vuelo:",vuelo[0]," - Piloto:", piloto[0]," - Asientos:", vuelo[2])

    else:

        print("No se encontro ningun vuelo con ese numero")

    conexion.commit()
    conexion.close()

def verVuelos():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM vuelo")
    vuelos=cursor.fetchall()

    cursor.execute(f"SELECT matricula FROM piloto WHERE id={vuelos[0][3]}")
    piloto=cursor.fetchone()

    if len(vuelos)>0:

        print("Vuelos:")

        for vuelo in vuelos:
            print("Vuelo:",vuelo[1]," - Piloto:", piloto[0]," - Asientos:", vuelo[2])

    else:

        print("No hay vuelos registrados")

#--------------------------------------------ASIGNAR VUELOS--------------------------------------------

def asignarVueloPasajero():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    dni=int(input("Ingrese el dni del pasajero que desea asignar a un vuelo(8 enteros): \n>>> "))
    while not fa.validarDni(dni):
        dni=int(input("Ingrese el dni del pasajero que desea asignar a un vuelo(8 enteros): \n>>> "))

    cursor.execute(f"SELECT id,nombre,apellido FROM pasajeros WHERE dni={dni}")
    pasajero=cursor.fetchone()

    if pasajero is not None:

        print("Pasajero:",pasajero[1],pasajero[2])

        numero=int(input("Ingrese el numero de vuelo a asignar (4 enteros): \n>>> "))
        while not fa.validarNumeroVuelo(numero):
            numero=int(input("Ingrese el numero de vuelo a asignar (4 enteros): \n>>> "))

        cursor.execute(f"SELECT id FROM vuelo WHERE numero={numero}")
        vuelo=cursor.fetchone()

        if vuelo is not None:
                
            cursor.execute("INSERT INTO pasajeros_vuelo VALUES (null,'{}','{}')".format(pasajero[0],vuelo))
            print("Vuelo y pasajeros asignados con exito")

        else:

            print("No existe vuelo con ese numero")

    else:

        print("No se encontro ningun pasajero con ese Dni")

    conexion.commit()
    conexion.close()

def verVuelosPasajeros():

    conexion=sqlite3.connect("sistemavuelos.db")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM pasajeros_vuelo")
    vuelos=cursor.fetchall()

    if len(vuelos)>0:

        print("Vuelos asignados:")

        for vuelo in vuelos:
            print("Vuelo: ",vuelo[1],"Pasajero:", vuelo[2])

    else:

        print("No hay vuelos asignados registrados")



