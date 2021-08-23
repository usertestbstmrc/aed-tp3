#!/usr/bin/python

"""
this module execute main program
"""

# MAIN
import modulo as m
from modulo import * #despues cambiar


def main():
    """contents all calls fuctions from modulo and user interact instances"""
    opcion = None
    while opcion != 8:
        mostrar_opciones()
        opcion = int(input('Ingrese su opción: '))
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            opcion4()
        elif opcion == 5:
            opcion5()
        elif opcion == 6:
            opcion6()
        elif opcion == 7:
            opcion7()
        print('==' * 18)
    # hasta ahora esta bien el menu
    print('¡Hasta luego!')


if __name__ == '__main__':
    main()
