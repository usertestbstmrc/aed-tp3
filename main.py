#!/usr/bin/python

"""
this module execute main program
"""

# MAIN
import modulo as m
from registro import Libro

def main():
    """contents all calls fuctions from modulo and user interact instances"""

    opcion = None
    while opcion != 8:
        m.mostrar_opciones()
        opcion = int(input('Ingrese su opción: '))
        print('\n')

        if opcion == 1:
            print("Generación y carga de libros")

            books_list_size = int(input('Cantidad de libros a ingresar al sistema: '))
            books = m.list_generator(books_list_size)
            opc_submenu = None

            while opc_submenu not in range(3):
                m.print_submenu_opc1()
                opc_submenu = int(input('|--> Ingrese su opción: '))
                book_index = -1

                if opc_submenu == 1:

                    for book in books:
                        book_index += 1

                        isbn_info = input('ISBN: ')
                        # FUNCION DE VALIDACIÓN DE MICA
                        title_info = input('TÍTULO: ')

                        gender_info = -1
                        while gender_info not in range(10):
                            m.gender_menu()
                            gender_info = int(input('SELECCIONE EL GÉNERO: '))

                        languaje_info = -1
                        while languaje_info not in range (1, 6):
                            m.languaje_menu()
                            languaje_info = int(input('IDIOMA: '))

                        price_info = float(input('PRECIO: '))

                        books[book_index] = Libro(isbn_info, title_info, gender_info, \
                                languaje_info, price_info)

                    break

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
