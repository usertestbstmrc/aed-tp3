#!/usr/bin/python

"""
this module execute main program
"""

# MAIN
import modulo as m


def main():
    """contents all calls fuctions from modulo and user interact instances"""

    opcion = None
    while opcion != 8:
        m.mostrar_opciones()
        opcion = int(input('Ingrese su opción: '))
        print('\n')

        if opcion == 1:
            print("Generación y carga de libros")
            opc_submenu = None

            while opc_submenu != -1:
                m.print_submenu_opc1()
                opc_submenu = int(input('|--> Ingrese su opción: '))

                if opc_submenu == 1:
                    m.opcion1_manual()

                elif opc_submenu == 2:
                    m.opcion1_automatica()

        elif opcion == 2:
            m.opcion2()
        elif opcion == 3:
            m.opcion3()
        elif opcion == 4:
            m.opcion4()
        elif opcion == 5:
            m.opcion5()
        elif opcion == 6:
            m.opcion6()
        elif opcion == 7:
            m.opcion7()
        print('==' * 18)
    # hasta ahora esta bien el menu
    print('¡Hasta luego!')


if __name__ == '__main__':
    main()
