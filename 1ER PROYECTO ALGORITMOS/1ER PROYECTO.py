"""
1ER PROYECTO ALGORITMOS Y ESTRUCTURAS 2
Annuar Abouharb #30.350.953
Jean Odriozola #29.569.900

"""

import csv
from datetime import datetime

#Algoritmos Quicksort
def quicksort(lista,aux):
    # Si la lista está vacía o tiene un solo elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    # Elegimos un elemento pivot (por ejemplo, el primer elemento de la lista)
    pivot = lista[0]

    # Dividimos la lista en tres partes: elementos menores, iguales y mayores que el pivot
    menores = []
    iguales = []
    mayores = []

    for elemento in lista:
        if elemento < pivot:
            menores.append(elemento)
        elif elemento == pivot:
            iguales.append(elemento)
        else:
            mayores.append(elemento)

    # Recursivamente ordenamos las partes menores y mayores
    menores_ordenados = quicksort(menores)
    mayores_ordenados = quicksort(mayores)

    if aux == True: #Ascendente
        return menores_ordenados + iguales + mayores_ordenados
    elif aux == False: #Descendente
        return mayores_ordenados + iguales + menores_ordenados

# Función de partición para Quicksort de Fechas
def particion(arr, bajo, alto):
    pivot = convertir_a_datetime(arr[alto])  # Elegir el último elemento como pivote
    i = bajo - 1  # Índice del elemento más pequeño

    for j in range(bajo, alto):
        if convertir_a_datetime(arr[j]) <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

# Función Quicksort para ordenar fechas
def quicksort_fechas(arr, bajo, alto):
    if bajo < alto:
        pi = particion(arr, bajo, alto)

        # Ordenar las sub-listas recursivamente
        quicksort_fechas(arr, bajo, pi - 1)
        quicksort_fechas(arr, pi + 1, alto)

# Función para convertir una fecha en un objeto datetime para comparación
def convertir_a_datetime(fecha):
    return datetime.strptime(fecha, "%d/%m/%Y")

def main():

    #Seleccion de hotel
    hesperia = 'hesperia.csv'
    lidotel = 'lidotel.csv'
    executive = 'executive.csv'
    hotel_aux = ''
    opcion = 0

    while True:
        print("Por favor seleccione un hotel: ")
        print("1. Hesperia")
        print("2. Lidotel")
        print("3. Executive")
        opcion = int(input()) 

        if opcion == 1:
            hotel_aux = hesperia
            break
        elif opcion == 2:
            hotel_aux = lidotel
            break
        elif opcion == 3:
            hotel_aux = executive
            break
        else:
            print("\nVuelve a intentarlo")

    #Eleccion de Orden (Ascendente o Descendente)
    orden = 0
    opcion = True
    while True:
        print("\nElige una opcion de orden: ")
        print("1. Ascendentemente")
        print("2. Descendetemente")
        orden = int(input())

        if orden == 1:
            opcion = True
            break
        elif orden == 2:
            opcion = False
            break
        else:
            print("\nOcurrio un error al ingresar una opcion")    
            
    #Lectura de archivos .csv
    with open(hotel_aux,'r') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=';')

        next(lector)
        next(lector)
        next(lector) #Se omiten las 3 primeras filas

        nombres = []
        reservas = []
        entradas = []
        salidas = []
        nros_habitaciones = []
        telefonos = []
        correos = []
        ids = []
        nro_reservas = []

        for columna in lector:

            nombres.append(columna[0])
            reservas.append(columna[1])
            entradas.append(columna[2])
            salidas.append(columna[3])
            nros_habitaciones.append(columna[4])
            telefonos.append(columna[9])
            correos.append(columna[10])
            ids.append(columna[17])
            nro_reservas.append(columna[18])

            """nombre = columna[0]
            reserva = columna[1]
            entrada = columna[2]
            salida = columna[3]
            nro_habitacion = columna[4]
            duracion = columna[5]
            tipo_habitacion = columna[6]
            preferencias_alimentarias = columna[7]
            nro_personas = columna[8]
            telefono = columna[9]
            correo = columna[10]
            precio = columna[11]
            metodo_pago = columna[12]
            notas = columna[13]
            estado = columna[14]
            check_in = columna[15]
            check_out = columna[16]
            id = columna[17]"""

        print("\n****** BIENVENIDO AL SISTEMA DE RESERVACIONES ******\n")
        #Informacion del menu
        if hotel_aux == "hesperia.csv":
            print("Hotel actual: Hesperia")
        elif hotel_aux == "lidotel.csv":
            print("Hotel actual: Lidotel")
        else:
            print("Hotel actual: Excecutive")
        
        if opcion == True:
            print("Orden de impresion por defecto: Ascendentemente")
        elif opcion == False:
            print("Orden de impresion por defecto: Descendentemente")

        decision = 0
        decision_2 = 0

        while True:
            print("\nSeleccione una opcion a realizar: ")
            print("1. Seleccion de Criterios de Ordenamiento (Quicksort)")
            print("2. Ordenamiento Multiple")
            print("3. Archivo de Configuracion")
            print("4. Funcionalidades Adicionales")
            print("5. Salir")
            decision = int(input())

            if decision == 1:
                
                print("Seleccione un elemento a ordenar: ")
                print("1. Fecha de Reserva")
                print("2. Fecha de Entrada")
                print("3. Fecha de Salida")
                print("4. Nro Habitacion")
                print("5. Duracion Estadia")
                print("6. Precio Total")
                decision_2 = int(input())

                if decision_2 == 1:
                    n = len(reservas)
                    quicksort_fechas(reservas,0,n - 1)
                    
                

            
main()