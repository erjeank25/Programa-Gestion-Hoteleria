"""
1ER PROYECTO ALGORITMOS Y ESTRUCTURAS 2
Annuar Abouharb #30.350.953
Jean Odriozola #29.569.900

"""

import csv
from datetime import datetime

def diccionario():
    persona = {
        "nombre": None,
        "reserva": None,
        "entrada": None,
        "salida": None,
        "nro habitacion": None,
        "estadia": None,
        "precio": None,
        "telefono": None,
        "correo": None,
        "id": None,
        "nro reserva": None,
    }
    return persona

#Algoritmos Quicksort
def quicksort(lista,parametro,aux):
    # Si la lista está vacía o tiene un solo elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    # Elegimos un elemento pivot (por ejemplo, el primer elemento de la lista)
    pivot = int(lista[0][parametro])

    # Dividimos la lista en tres partes: elementos menores, iguales y mayores que el pivot
    menores = []
    iguales = []
    mayores = []

    for elemento in lista:
        if int(elemento[parametro]) < pivot:
            menores.append(elemento)
        elif int(elemento[parametro]) == pivot:
            iguales.append(elemento)
        elif int(elemento[parametro]) > pivot:
            mayores.append(elemento)
    # Recursivamente ordenamos las partes menores y mayores
    menores_ordenados = quicksort(menores,parametro,aux)
    mayores_ordenados = quicksort(mayores,parametro,aux)

    if aux == True: #Ascendente
        return menores_ordenados + iguales + mayores_ordenados
    else: #Descendente
        return mayores_ordenados + iguales + menores_ordenados

# Función de partición para Quicksort de Fechas
def particion(arr, bajo, alto,parametro,aux):
    pivot = convertir_a_datetime(arr[alto][parametro])  # Elegir el último elemento como pivote
    i = bajo - 1  # Índice del elemento más pequeño

    if aux == True: #Ascendente
        for j in range(bajo, alto):
            if convertir_a_datetime(arr[j][parametro]) <= pivot: #ojo
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1
    else:           #Descendente
        for j in range(bajo, alto):
            if convertir_a_datetime(arr[j][parametro]) >= pivot: #ojo
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1        


# Función Quicksort para ordenar fechas
def quicksort_fechas(arr, bajo, alto,parametro,aux):
    if bajo < alto:
        pi = particion(arr, bajo, alto,parametro,aux)

        # Ordenar las sub-listas recursivamente
        quicksort_fechas(arr, bajo, pi - 1,parametro,aux)
        quicksort_fechas(arr, pi + 1, alto,parametro,aux)

# Función para convertir una fecha en un objeto datetime para comparación
def convertir_a_datetime(fecha):
    return datetime.strptime(fecha, "%d/%m/%Y")









def ordenamiento(database,orden):

    print("\nSeleccione un elemento a ordenar: ")
    print("1. Fecha de Reserva")
    print("2. Fecha de Entrada")
    print("3. Fecha de Salida")
    print("4. Nro Habitacion")
    print("5. Duracion Estadia")
    print("6. Precio Total")
    print("7. Regresar")
    decision = int(input())

    if decision == 1:
        print("")
        n = len(database)
        parametro = "reserva"
        quicksort_fechas(database,0,n-1,parametro,orden)
        for registro in database:
            print(registro["nombre"],registro["reserva"], registro["telefono"],registro["correo"],registro["id"])
    elif decision == 2:
        print("")        
        n = len(database)
        parametro = "entrada"
        quicksort_fechas(database,0,n-1,parametro,orden)
        for registro in database:
            print(registro["nombre"],registro["entrada"], registro["telefono"],registro["correo"],registro["id"])
    elif decision == 3:
        print("")        
        n = len(database)
        parametro = "salida"
        quicksort_fechas(database,0,n-1,parametro,orden)
        for registro in database:
            print(registro["nombre"],registro["salida"], registro["telefono"],registro["correo"],
                registro["id"])
    elif decision == 4:
        print("")        
        n = len(database)
        parametro = "nro habitacion"
        ordenado = quicksort(database,parametro,orden)
        for registro in ordenado:
            print(registro["nombre"],registro["nro habitacion"], registro["telefono"],registro["correo"],registro["id"])
    elif decision == 5:
        print("")        
        n = len(database)
        parametro = "estadia"
        ordenado = quicksort(database,parametro,orden)
        for registro in ordenado:
            print(registro["nombre"],registro["estadia"], registro["telefono"],registro["correo"],registro["id"])                                                     
    elif decision == 6:
        print("")        
        n = len(database)
        parametro = "precio"
        ordenado = quicksort(database,parametro,orden)
        for registro in ordenado:
            print(registro["nombre"],registro["precio"], registro["telefono"],registro["correo"],
                registro["id"])
    elif decision == 7:
        return                                     
                        
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
    orden = 0 #VARIABLE IMPORTANTE
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

        database = []

        for columna in lector: #lectura del csv
            persona = diccionario()
            persona["nombre"] = columna[0]
            persona["reserva"] = columna[1]
            persona["entrada"] = columna[2]
            persona["salida"] = columna[3]
            persona["nro habitacion"] = columna[4]
            persona["estadia"] = columna[5]
            persona["telefono"] = columna[9]
            persona["correo"] = columna[10]
            persona["precio"] = columna[11]
            persona["id"] = columna[17]
            persona["nro reserva"] = columna[18]
            database.append(persona)
        print(database)

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
        #opciones a realizar
        while True:
            print("\nSeleccione una opcion a realizar: ")
            print("1. Seleccion de Criterios de Ordenamiento (Quicksort)")
            print("2. Ordenamiento Multiple")
            print("3. Archivo de Configuracion")
            print("4. Funcionalidades Adicionales")
            print("5. Salir")
            decision = int(input())

            if decision == 1:
                ordenamiento(database,orden)
            
                     
main()