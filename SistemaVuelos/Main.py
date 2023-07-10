import SistemaVuelos as sv
import FuncionesAuxiliares as fa

sv.crearBD()

print("-------------Gestor de vuelos-------------")

while True:

    print("------------------------------------------")
    print("Seleccione la opcion a realizar:")
    print("")

    print("1) Gestionar pasajeros \n2) Gestionar pilotos \n3) Gestionar vuelos \n4) Borrar todos los datos de la base de datos \n5) Salir")
    opcion=int(input(">>> "))

    print("")
    fa.limpiarPantalla()

    if opcion==1:

        while True:

            print("")
            print("1) Agregar pasajero \n2) Borrar pasajero \n3) Consultar pasajero \n4) Ver pasajeros \n5) Volver al menu principal")
            opcionPasajero=int(input(">>> "))

            print("")
            fa.limpiarPantalla()

            if opcionPasajero==1:

                sv.ingresarPasajero()

            elif opcionPasajero==2:

                sv.borrarPasajero()

            elif opcionPasajero==3:

                sv.consultarPasajero()

            elif opcionPasajero==4:

                sv.verPasajeros()

            elif opcionPasajero==5:

                break

            else:

                print("Opcion incorrecta")
    
    elif opcion==2:

        while True:

            print("")
            print("1) Agregar piloto \n2) Borrar piloto \n3) Consultar piloto \n4) Ver pilotos \n5) Volver al menu principal")
            opcionPiloto=int(input(">>> "))

            print("")
            fa.limpiarPantalla()

            if opcionPiloto==1:

                sv.ingresarPiloto()

            elif opcionPiloto==2:

                sv.borrarPiloto()

            elif opcionPiloto==3:

                sv.consultarPiloto()

            elif opcionPiloto==4:

                sv.verPilotos()

            elif opcionPiloto==5:

                break

            else:

                print("Opcion incorrecta")

    elif opcion==3:

        while True:

            print("")
            print("1) Agregar vuelo \n2) Borrar vuelo \n3) Consultar vuelo \n4) Ver vuelos \n5) Asignar pasajeros \n6) Ver asignacion de vuelos \n7) Volver al menu principal")
            opcionVuelo=int(input(">>> "))

            print("")
            fa.limpiarPantalla()

            if opcionVuelo==1:

                sv.ingresarVuelo()

            elif opcionVuelo==2:

                sv.borrarVuelo()

            elif opcionVuelo==3:

                sv.consultarVuelo()

            elif opcionVuelo==4:

                sv.verVuelos()

            elif opcionVuelo==5:

                sv.asignarVueloPasajero()

            elif opcionVuelo==6:

                sv.verVuelosPasajeros()

            elif opcionVuelo==7:

                break

            else:

                print("Opcion incorrecta")

    elif opcion==4:

        sv.borrarBD()

    elif opcion==5:

        break

    else:

        print("Opcion incorrecta")

    