#!/usr/bin/python

"""
this module execute main program
"""

# MAIN
import modulo as m
from registro import Libro

def main():
    """contents all calls fuctions from modulo and user interact instances"""

    books = []
    gen_final = ''
    vector_cargado = False
    opcion = None
    while opcion != 8:
        m.mostrar_opciones()
        opcion = int(input('Ingrese su opción: '))
        print('\n')

        if opcion == 1:
            print("Generación y carga de libros")
            #validar books_list_size
            books_list_size = m.validar_carga(0, 'Cantidad de libros a ingresar al sistema: ')
            books = m.list_generator(books_list_size)
            opc_submenu = None
            vector_cargado = True

            while opc_submenu not in range(3):
                m.print_submenu_opc1()
                opc_submenu = int(input('|--> Ingrese su opción: '))
                book_index = -1

                if opc_submenu == 1:

                    for book in books:
                        book_index += 1

                        isbn_info = ''
                        isbn_valid_format = False
                        isbn_valid_math_rel = False

                        while not isbn_valid_format or not isbn_valid_math_rel:

                            isbn_info = input('ISBN: ')
                            isbn_valid_format, msj_format = m.validate_isbn_format(isbn_info)
                            isbn_valid_math_rel, msj_math = m.validate_isbn_math_relation(isbn_info)

                            if not isbn_valid_format:
                                print('ERROR DE FORMATO: ', msj_format)

                            if not isbn_valid_math_rel:
                                print('ERROR MATEMÁTICO: ', msj_math)

                        title_info = input('TÍTULO: ')

                        gender_info = -1
                        while gender_info not in range(10):
                            m.gender_menu()
                            gender_info = int(input('SELECCIONE EL GÉNERO: '))
                            gen_final = m.recorrer_gen(gender_info)

                        language_info = -1
                        while language_info not in range (1, 6):
                            m.language_menu()
                            language_info = int(input('IDIOMA: '))

                        price_info = float(input('PRECIO: '))

                        books[book_index] = Libro(isbn_info, title_info, gen_final, \
                                language_info, price_info)

                elif opc_submenu == 2:
                    m.opcion1_automatica(books)

        elif opcion == 2:
            m.opcion2(books, vector_cargado)

        elif opcion == 3:
            m.opcion3(books, vector_cargado)
        elif opcion == 4:
            m.opcion4(books)
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
