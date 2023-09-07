"""
1ER PROYECTO ALGORITMOS Y ESTRUCTURAS 2
Annuar Abouharb #30.350.953
Jean Odriozola #29.569.900

"""

import csv

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
            print("Vuelve a intentarlo")

    #lectura de archivos .csv
    with open(hotel_aux,'r') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=';')

        for columna in lector:
            nombre = columna[0]
            reserva = columna[1]
            entrada = columna[2]
            salida = columna[3]
            nro_habitacion = columna[4]
            duracion = columna[5]
            tipo_habitacion = columna[6]
            preferencias_alimentarias = columna[7]
            nro_personas = columna[8]
            correo = columna[9]
            precio = columna[10]
            metodo_pago = columna[11]
            notas = columna[12]
            estado = columna[13]
            check_in = columna[14]
            check_out = columna[15]
            id = columna[16]
            print(nombre)

        print("\n****** BIENVENIDO AL SISTEMA DE RESERVACIONES ******")
        if hotel_aux == "hesperia.csv":
            print("Hotel actual: Hesperia")
        elif hotel_aux == "lidotel.csv":
            print("Hotel actual: Lidotel")
        else:
            print("Hotel actual: Excecutive")

        while True:
            print("Seleccione una opcion a realizar: ")
            print("1. Seleccion de Criterios de Ordenamiento")
            print("2. Ordenamiento Multiple")
            print("3. Archivo de Configuracion")
main()