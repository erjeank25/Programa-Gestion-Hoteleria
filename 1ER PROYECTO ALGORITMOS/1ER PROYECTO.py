"""
1ER PROYECTO ALGORITMOS Y ESTRUCTURAS 2
Annuar Abouharb #30.350.953
Jean Odriozola #29.569.900

"""

import csv #Usada para manipular el archivo.csv y configuracion.csv
import os #Usada para gestionar archivos y directorios
import shutil #Usada en este caso para copiar archivos
from datetime import datetime #Usada para manipular fechas y horas


#Variables globales usadas para determinar el orden (ascen o descen), detalles del hotel y
#ruta por defecto


descripcion = ""
ruta_defecto = ""

def diccionario(): #Diccionario para almacenar los valores del archivo hotel.csv
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
    }
    return persona

def diccionario_de_numero_reservaciones(): #Diccionario extra para guardar el numero de reservaciones de cada persona.
    numero_reservacion = {
        "nombre": None,
        "nro reservaciones": None,
        "telefono": None,
        "correo": None,
        "id": None
    }
    return numero_reservacion



def diccionario_config(): #Diccionario para almacenar los valores del archivo configuracion.csv
    modalidades = {
        "defecto": None,
        "detalles": None,
        "ruta": None
    }
    return modalidades

#Algoritmo Quicksort
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

# Metodo de partición para Quicksort de Fechas
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


# Algoritmo Quicksort para ordenar fechas
def quicksort_fechas(arr, bajo, alto,parametro,aux):
    if bajo < alto:
        pi = particion(arr, bajo, alto,parametro,aux)

        # Ordenar las sub-listas recursivamente
        quicksort_fechas(arr, bajo, pi - 1,parametro,aux)
        quicksort_fechas(arr, pi + 1, alto,parametro,aux)

# Metodo para convertir una fecha en un objeto datetime para comparación
def convertir_a_datetime(fecha):
    return datetime.strptime(fecha, "%d/%m/%Y")

#Algoritmo Mergesort
def mergesort(database, parametro,orden):
    if len(database) > 1:
        medio = len(database) // 2
        mitad_izquierda = database[:medio]
        mitad_derecha = database[medio:]

        mergesort(mitad_izquierda, parametro,orden)
        mergesort(mitad_derecha, parametro,orden)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if orden == True:
                if mitad_izquierda[i][parametro] < mitad_derecha[j][parametro]:
                    database[k] = mitad_izquierda[i]
                    i += 1
                else:
                    database[k] = mitad_derecha[j]
                    j += 1
                k += 1
            elif orden == False:
                if mitad_izquierda[i][parametro] > mitad_derecha[j][parametro]:
                    database[k] = mitad_izquierda[i]
                    i += 1
                else:
                    database[k] = mitad_derecha[j]
                    j += 1
                k += 1                    

        while i < len(mitad_izquierda):
            database[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            database[k] = mitad_derecha[j]
            j += 1
            k += 1


def heapify(arr,n,i,parametro,orden): #Algoritmo de apoyo de Heapsort
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if orden:
        if l < n and int(arr[l][parametro]) > int(arr[largest][parametro]):
            largest = l
        if r < n and int(arr[r][parametro]) > int(arr[largest][parametro]):
            largest = r
    else:
        if l < n and int(arr[l][parametro]) < int(arr[largest][parametro]):
            largest = l
        if r < n and int(arr[r][parametro]) < int(arr[largest][parametro]):
            largest = r
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest,parametro,orden)

def heapsort(arr,parametro,orden): #Algoritmo Heapsort
    n = len(arr)
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i,parametro,orden)
    for i in range(n - 1,0,-1):
        arr[i] , arr[0] = arr[0] , arr[i]
        heapify(arr,i,0,parametro,orden)

def shellsort(ocurrencias,orden):
    n = len(ocurrencias)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp_nombre, temp_datos = ocurrencias[i]
            j = i
            if orden: #Ascendente
                while j >= intervalo and temp_datos['apariciones'] < ocurrencias[j - intervalo][1]['apariciones']:
                    ocurrencias[j] = ocurrencias[j - intervalo]
                    j -= intervalo
            else: #Descendente
                while j >= intervalo and temp_datos['apariciones'] > ocurrencias[j - intervalo][1]['apariciones']:
                    ocurrencias[j] = ocurrencias[j - intervalo]
                    j -= intervalo                        
            ocurrencias[j] = (temp_nombre, temp_datos)
        intervalo //= 2

def ordenamiento(database,orden):

    #Se selecciona un elemento por el cual se van a filtrar los datos mas importante
    print("\nSeleccione un elemento a ordenar: ")
    print("1. Fecha de Reserva")
    print("2. Fecha de Entrada")
    print("3. Fecha de Salida")
    print("4. Nro Habitacion")
    print("5. Duracion Estadia")
    print("6. Precio Total")
    print("7. Regresar")
    decision = int(input())

    #Reserva
    if decision == 1:
        print("")
        n = len(database)
        parametro = "reserva"
        quicksort_fechas(database,0,n-1,parametro,orden)
        print("Nombre    Fecha de reservacion    Numero de telefono          Correo electronico            ID")
        print("")
        for registro in database:
            print("{:<14} {:20} {:21} {:<32} {:<7}".format(registro["nombre"], registro["reserva"], registro["telefono"],registro["correo"],registro["id"]))
    #Entrada
    elif decision == 2:
        print("")        
        n = len(database)
        parametro = "entrada"
        quicksort_fechas(database,0,n-1,parametro,orden)
        print("Nombre       Fecha de entrada    Numero de telefono          Correo electronico             ID")
        print("")
        for registro in database:
            print("{:<14} {:20} {:21} {:<32} {:<7}".format(registro["nombre"], registro["entrada"], registro["telefono"],registro["correo"],registro["id"]))
    #Salida
    elif decision == 3:
        print("")        
        n = len(database)
        parametro = "salida"
        quicksort_fechas(database,0,n-1,parametro,orden)
        print("Nombre       Fecha de salida     Numero de telefono          Correo electronico             ID")
        print("")
        for registro in database:
            print("{:<14} {:20} {:21} {:<32} {:<7}".format(registro["nombre"], registro["salida"], registro["telefono"],registro["correo"],registro["id"]))
    #Nro Habitacion
    elif decision == 4:
        print("")        
        n = len(database)
        parametro = "nro habitacion"
        ordenado = quicksort(database,parametro,orden)
        print("Nombre      Numero de habitacion       Numero de telefono        Correo electronico                ID")
        print("")
        for registro in ordenado:
            print("{:<14} {:^20} {:^24} {:36} {:<7}".format(registro["nombre"], registro["nro habitacion"], registro["telefono"],registro["correo"],registro["id"]))
    #Estadia
    elif decision == 5:
        print("")        
        n = len(database)
        parametro = "estadia"
        ordenado = quicksort(database,parametro,orden)
        print("Nombre       Duracion de Estadia      Numero de telefono        Correo electronico                ID")
        print("")
        for registro in ordenado:
            print("{:<11} {:^21} {:^26} {:36} {:<7}".format(registro["nombre"], registro["estadia"], registro["telefono"],registro["correo"],registro["id"]))                                                    
    #Precio
    elif decision == 6:
        print("")        
        n = len(database)
        parametro = "precio"
        ordenado = quicksort(database,parametro,orden)
        print("Nombre        Precio      Numero de telefono       Correo electronico                ID")
        print("")
        for registro in ordenado:
            print("{:<11} {:^11} {:^24} {:34} {:<7}".format(registro["nombre"], registro["precio"], registro["telefono"],registro["correo"],registro["id"]))
    #Salir
    elif decision == 7:
        return                                     

def multiple(database,orden):
        
        filtrados = [] #Creacion de un array para meter los diccionarios filtrados
        eleccion = 0 #Variable para eleccion
        filtro = 0  #Usado para ingresar fechas a filtrar
        
        #Se escoge un filtro a manera de embudo
        
        print("\nEscoge el primer filtro: ")
        print("1. Fecha de Reserva")
        print("2. Fecha de Entrada")
        print("3. Fecha de Salida")
        print("4. Regresar")
        eleccion = int(input())

        #Embudo Reserva
        if eleccion == 1: 
            print("\nIntroduce una Fecha de Reserva para filtrar. Ejemplo (dd/mm/aaaa)")
            filtro = input()
            for i in database:
                if i.get('reserva') == filtro:
                    filtrados.append(i)
        #Embudo Entrada            
        elif eleccion == 2: 
            print("\nIntroduce una Fecha de Entrada para filtrar. Ejemplo (dd/mm/aaaa)")
            filtro = input()
            for i in database:
                if i.get('entrada') == filtro:
                    filtrados.append(i)
        #Embudo Salida            
        elif eleccion == 3: 
            print("\nIntroduce una Fecha de Salida para filtrar. Ejemplo (dd/mm/aaaa)")
            filtro = input()
            for i in database:
                if i.get('salida') == filtro:
                    filtrados.append(i)
        #Salir            
        elif eleccion == 4:
            return
        else:
            print("Error al introducir una opcion")

        eleccion2 = 0

        n = len(filtrados)

        #Se escoge un termino a ordenar (ya teniendo un filtro)        
        print("Escoge el elemento a ordenar:")
        print("1. Nro Habitacion")
        print("2. Duracion Estadia")
        print("3. Precio Total") 
        eleccion2 = int(input())

        #Nro Habitacion
        if eleccion2 == 1:
            parametro = "nro habitacion"
            ordenado = quicksort(filtrados,parametro,orden)
            print()
            print("Nombre      Numero de habitacion       Numero de telefono        Correo electronico                ID")
            print("")
            for registro in ordenado:
                print("{:<14} {:^20} {:^24} {:36} {:<7}".format(registro["nombre"], registro["nro habitacion"], registro["telefono"],registro["correo"],registro["id"]))
        #Estadia
        elif eleccion2 == 2:
            parametro = "estadia"
            ordenado = quicksort(filtrados,parametro,orden)
            print()
            print("Nombre       Duracion de Estadia      Numero de telefono        Correo electronico                ID")
            print("")
            for registro in ordenado:
                print("{:<11} {:^21} {:^26} {:36} {:<7}".format(registro["nombre"], registro["estadia"], registro["telefono"],registro["correo"],registro["id"]))             
        #Precio
        elif eleccion2 == 3:
            parametro = "precio"
            ordenado = quicksort(filtrados,parametro,orden)
            print()
            print("Nombre        Precio      Numero de telefono       Correo electronico                ID")
            print("")
            for registro in ordenado:
                print("{:<11} {:^11} {:^24} {:34} {:<7}".format(registro["nombre"], registro["precio"], registro["telefono"],registro["correo"],registro["id"]))
        else:
            print("Error al introducir una opcion")                                            

def archivo(orden, descripcion,ruta_defecto):

    config = [] #Array usado para llenarlo de diccionarios del archivo configuracion.csv

    with open('configuracion.csv','r') as archivo_csv: #Lectura del archivo configuracion.csv
        lector = csv.reader(archivo_csv, delimiter=';')
        next(lector) #Se omite el primer registro del archivo de configuracion

        for i in lector: #Ciclo para llenar el array de diccionarios
            modalidades = diccionario_config()
            modalidades["defecto"] = i[0]
            modalidades["detalles"] = i[1]
            modalidades["ruta"] = i[2]
            config.append(modalidades)  

    decision = 0 #Variable de decision

    #Se pregunta si el usuario quiere ordenar de manera ascendente o descendente
    print("\nSeleccione un orden: ")
    print("Orden actual: ",orden)
    print("1. Ascendente") 
    print("2. Descendente")
    decision = int(input())

    if decision == 1:
        for i in config:
            if i.get("defecto") == "True":
                orden = True
                break
    elif decision == 2:
        for i in config:
            if i.get("defecto") == "False":
                orden = False
                break      
    else:
        print("\nVuelva a introducir una opcion")    

    decision1 = 0 #Variable de decision
    #Se pregunta si desea mantener el mensaje actual
    print("\nDesea mantener el mensaje actual o cambiarlo?")
    print("Mensaje: ",descripcion)
    print("1. Defecto")
    print("2. Cambiar al Hesperia")
    print("3. Cambiar al Carlton")
    decision1 = int(input())

    if decision1 == 1:
        descripcion = descripcion
    if decision1 == 2:
        for i in config:
            if i.get("detalles") == "Hotel Hesperia, 4 Estrellas, Valencia":
                descripcion = "Hotel: Hesperia, 4 Estrellas, Valencia"
    elif decision1 == 3:
        for i in config:
            if i.get("detalles") == "Hotel Carlton, 5 Estrellas, Nueva York":
                descripcion = "Hotel: Carlton, 5 Estrellas, Nueva York"
    else:
        print("\nVuelva a introducir una opcion")   

    decision2 = 0 #Variable de decision
    #Se pregunta si se desea cambiar la ruta del archivo.csv
    print("\nDesea mantener la ruta actual o cambiarla a otra opcion?")
    print("Ruta: ",ruta_defecto)
    print("1. Defecto")
    print("2. Cambiar a Carpeta 1")
    print("3. Cambiar a Carpeta 2")

    decision2 = int(input())

    if decision2 == 1:
        ruta_defecto = ruta_defecto
    elif decision2 == 2:
        for i in config:
            if i.get("ruta") == 'Documentos':
                ruta_nueva = 'C:\\Users\jodri\\OneDrive\\Escritorio\\Carpeta Prueba 1' #Se puede modificar la ruta a conveniencia
                shutil.copy(ruta_defecto,ruta_nueva) #Se copia la el archivo a una nueva ruta
                ruta_defecto = ruta_nueva  

    elif decision2 == 3:
        for i in config:
            if i.get("ruta") == 'Descargas':
                ruta_nueva = 'C:\\Users\\jodri\\OneDrive\\Escritorio\\Carpeta Prueba 2' #Se puede modificar la ruta a conveniencia
                shutil.copy(ruta_defecto,ruta_nueva) #Se copia la el archivo a una nueva ruta
                ruta_defecto = ruta_nueva
    else:
        print("\nVuelva a introducir una opcion")              
   
    return orden, descripcion, ruta_defecto

def adicionales(database,orden):

    eleccion = 0

    print("Seleccione una opcion:")
    print("1. Ordenamiento por Rango (Mergesort)")
    print("2. Clientes por numero de reservaciones realizadas (Shellsort)")
    print("3. Reservaciones segun su duracion de estadia (Heapsort)")
    eleccion = int(input())

    if eleccion == 1:
    
        #Se introducen 2 fechas de reservas para filtrar como embudo
        filtrados = []   
        print("\nIntroduce el rango inferior de una Fecha de Reserva para filtrar. Ejemplo (dd/mm/aaaa)")
        filtro_1 = input()
        print("\nIntroduce el rango superior de una Fecha de Reserva para filtrar. Ejemplo (dd/mm/aaaa)")
        filtro_2 = input()

        #Se convierten las cadenas a fechas para compararlas
        parseo_1 = datetime.strptime(filtro_1, "%d/%m/%Y")
        parseo_2 = datetime.strptime(filtro_2, "%d/%m/%Y")

        #Se convierten las fechas de los diccionarios y se comparan con los filtros
        for i in database:
            parseo_principal = datetime.strptime(i.get('reserva'), "%d/%m/%Y") 
            if parseo_1 <= parseo_principal <= parseo_2:
                filtrados.append(i)   

        #Finalmente se orden las fechas filtradas por su rango de precio
        parametro = "precio"
        #Se hace uso del Algoritmo Mergesort
        mergesort(filtrados,parametro,orden)
        print("Nombre        Precio      Numero de telefono       Correo electronico                ID")
        print("")
        for registro in filtrados:
            print("{:<11} {:^11} {:^24} {:34} {:<7}".format(registro["nombre"], registro["precio"], registro["telefono"],registro["correo"],registro["id"])) 

    elif eleccion == 2:
        # Inicializar un diccionario para contar las ocurrencias de nombres
        ocurrencias = {}

        # Contar las ocurrencias de nombres
        for cliente in database:
            nombre = cliente['nombre']
            if nombre in ocurrencias:
                ocurrencias[nombre]['apariciones'] += 1
            else:
                ocurrencias[nombre] = {
                    'apariciones': 1,
                    'id': cliente['id'],
                    'correo': cliente['correo'],
                    'telefono': cliente['telefono']
                }

        # Conversion de diccionario a tupla
        lista = list(ocurrencias.items())
        # Aplicar Shellsort a las ocurrencias en forma de tupla       
        shellsort(lista,orden)

        # Imprimir el nombre de cada persona y la cantidad de veces que apareció, ordenado por las ocurrencias
        print("")
        print("Nombre        Nro Reservaciones       Numero de telefono        Correo electronico                 ID")
        for nombre, datos in lista:
            print("{:<11} {:^21} {:^26} {:36} {:<7}".format(nombre,datos["apariciones"],datos["telefono"],datos["correo"],datos["id"]))

    elif eleccion == 3:
        print("")
        parametro = "estadia"
        heapsort(database,parametro,orden)
        print("Nombre       Duracion de Estadia      Numero de telefono        Correo electronico                ID")
        print("")
        for registro in database:
            print("{:<11} {:^21} {:^26} {:36} {:<7}".format(registro["nombre"], registro["estadia"], registro["telefono"],registro["correo"],registro["id"]))

    else:
        print("Dato introducido invalido. Intente de nuevo")

def main():
    try:
        #Seleccion de hotel
        hotel = 'hotel.csv'

        #Ruta por defecto del archivo .csv
        ruta_defecto = os.path.join(os.getcwd(),hotel)

        #Eleccion de Orden (Ascendente o Descendente)
        while True:
            print("\nElige una opcion de orden: ")
            print("1. Ascendentemente")
            print("2. Descendetemente")
            opcion = int(input())

            if opcion == 1:
                orden = True
                break
            elif opcion == 2:
                orden = False
                break
            else:
                print("\nOcurrio un error al ingresar una opcion")    
                
        #Lectura de archivos .csv
        with open(ruta_defecto,'r') as archivo_csv: #Lectura del archivo hotel.csv
            lector = csv.reader(archivo_csv, delimiter=';')

            next(lector) #Se omiten la primera fila del archivo.csv

            database = [] #Se usa el array para guardar diccionarios de cada registro

            for columna in lector: #lectura del csv y creacion de diccionarios a agregarse en el array
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
                database.append(persona)

            #Se puede usar este print para verificar toda la base de datos
            #print(database)

            #Se agregar una descripcion inicial
            descripcion = 'Hotel Intercontinental, 4 estrellas, Valencia'

            while True:
                #Informacion del menu
                print("\n****** BIENVENIDO AL SISTEMA DE RESERVACIONES ******\n")

                if orden == True:
                    print("Orden de impresion por defecto: Ascendentemente")
                elif orden == False:
                    print("Orden de impresion por defecto: Descendentemente")

                print("Descripcion: ",descripcion)
                print("Ruta: ",ruta_defecto)

                decision = 0
                #Opciones a realizar
                print("\nSeleccione una opcion a realizar: ")
                print("1. Seleccion de Criterios de Ordenamiento (Quicksort)")
                print("2. Ordenamiento Multiple")
                print("3. Archivo de Configuracion")
                print("4. Funcionalidades Adicionales")
                print("5. Salir")
                decision = int(input())

                if decision == 1:
                    ordenamiento(database,orden)
                elif decision == 2:
                    multiple(database,orden)
                elif decision == 3:
                    #Se retornan los valores en forma de tupla al llamar al metodo
                    orden, descripcion, ruta_defecto = archivo(orden, descripcion, ruta_defecto)
                elif decision == 4:
                    adicionales(database,orden)
                elif decision == 5:
                    print("\nGracias por usar el programa :)")
                    break
                else:
                    print("\nError al introducir una opcion")    
    except ValueError:
        print("Solo se permiten numeros enteros")
    except Exception as e:
        print("Error: ",e,". Intente de nuevo...")
main()