"""
PSEUDOCÓDIGO: Sistema de Finanzas Personales

INICIO

    Inicio del sistema de finanzas personales importando logging y os
    LOGGING: Configura el registro de eventos en el archivo 'finanzas.log'
    OS: Crea una función para limpiar la pantalla según el sistema operativo
    Se crea una lista vacía para almacenar los gastos

MIENTRAS el usuario no quiera salir del programa:

    LIMPIAR PANTALLA
    IMPRIMIR "Bienvenido al sistema de FINANZAS PERSONALES"
    IMPRIMIR "1. Añadir gasto"
    IMPRIMIR "2. Ver resumen de gastos"
    IMPRIMIR "3. Salir del programa"

    SOLICITAR opcion al usuario

    SI opcion es "1":
        LIMPIAR PANTALLA
        SOLICITAR al usuario el concepto del gasto
        SOLICITAR al usuario la cantidad del gasto
        MIENTRAS la cantidad no sea válida:
            SOLICITAR al usuario la cantidad del gasto
            SI cantidad NO es un número positivo:
                LOGGING: Registrar error en el archivo 'finanzas.log'
            SI cantidad no es un número válido:
                LOGGING: Registrar error en el archivo 'finanzas.log'
                IMPRIMIR "Error: Por favor, introduzca un número válido."
        
        AÑADIR gasto a la lista de gastos
        LOGGING: Registrar gasto añadido en el archivo 'finanzas.log'
        IMPRIMIR "Gasto añadido correctamente."
        ESPERAR a que el usuario presione Enter para continuar

    SI NO SI opcion es "2":
        LIMPIAR PANTALLA

        SI hay gastos registrados:
            IMPRIMIR resumen de gastos con formato de tabla
            CALCULAR total de gastos
             PARA gasto EN gastos:
                IMPRIMIR concepto y cantidad del gasto
            IMPRIMIR total de gastos
        SINO:
            IMPRIMIR "No hay gastos registrados."
        
        ESPERAR a que el usuario presione Enter para continuar

    SI NO SI opcion es "3":
        LIMPIAR PANTALLA
        LOGGING: Registrar salida del sistema en el archivo 'finanzas.log'
        IMPRIMIR "Gracias por usar el sistema de FINANZAS PERSONALES. ¡Hasta luego!"
        SALIR DEL SISTEMA

    SINO:
        LOGGING: Registrar opción de menú no válida en el archivo 'finanzas.log'
        IMPRIMIR "Opción no válida. Seleccione 1, 2 o 3."
        ESPERAR a que el usuario presione Enter para continuar

FIN

"""

import os
import logging

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

logging.basicConfig(filename='finanzas.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("El sistema ha sido iniciado correctamente.")

gastos = []

while True:
    clear_screen()
    
    
    print("Bienvenido al sistema de FINANZAS PERSONALES")    
    print("")
    print("1. Añadir gasto")
    print("2. Ver resumen de gastos")
    print("3. Salir del programa")
    print("")

    opcion = input("Seleccione una opción: 1, 2 o 3: ")

    if opcion == "1":
        clear_screen()
        concepto = input("Introduzca el concepto del gasto: ")
        while True:
            try:
                cantidad = float(input("Introduzca la cantidad del gasto en euros: "))
                if not 0 < cantidad < float("inf"):
                    raise ValueError("La cantidad debe ser un número positivo.")
                break
            except ValueError:
                logging.error("Error: El usuario introdujo un valor no válido para la cantidad del gasto.")
                print("Error: Por favor, introduzca un número válido.")
        
        gastos.append({"concepto": concepto, "cantidad": cantidad})
        logging.info(f"Gasto añadido: {concepto} - {cantidad:.2f}€")
        print("")
        print("Gasto añadido correctamente.")
        print("")
        input("Presione Enter para continuar...")

    elif opcion == "2":
        clear_screen()

        if gastos:
            print("Resumen de Gastos:")
            print("")
            total_gastos = 0
            ancho_concepto = max(len(gasto["concepto"]) for gasto in gastos)
            ancho_cantidad = max(len(f"{gasto['cantidad']:.2f}€") for gasto in gastos)
            print(f"| {'Concepto'.ljust(ancho_concepto)} |   Cantidad  |")
            print("-" * (ancho_concepto + 16))
            
            for gasto in gastos:
                concepto = gasto['concepto'].capitalize().ljust(ancho_concepto)
                cantidad = f"{gasto['cantidad']:.2f}€".rjust(ancho_cantidad)

                print(f"| {concepto} | {cantidad} |")
                total_gastos += gasto["cantidad"]
                
                print("-" * (ancho_concepto + ancho_cantidad + 7))    

            print(f"\nTotal de gastos: {total_gastos:.2f}€")
            print("")

        else:
            print("No hay gastos registrados.")
        input("Presione Enter para continuar...")
    
    elif opcion == "3":
        clear_screen()
        logging.info("El usuario ha salido del programa.")
        print("Gracias por usar el sistema de FINANZAS PERSONALES. ¡Hasta luego!")
        break
    else:
        logging.error(f"Opción de menú no válida: {opcion}")
        print("Opción no válida. Seleccione 1, 2 o 3.")
        input("Presione Enter para continuar...")
