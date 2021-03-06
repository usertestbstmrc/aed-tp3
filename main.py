#!/usr/bin/python

"""
this module execute main program
"""

# MAIN mica
import modulo as m
from registro import Libro

def main():
    """contents all calls fuctions from modulo and user interact instances"""

    books = []
    cant = []
    gen_final = ''
    leng_final = ''
    vector_cargado = False
    opcion = None
    vec_cant = False
    while opcion != 8:
        m.mostrar_opciones()
        opcion = int(input('Ingrese su opción: '))
        print('==' * 18)
        if opcion == 1:
            #validar books_list_size
            books_list_size = m.validar_carga(0, 'Cantidad de libros a ingresar al sistema: ')
            books = m.list_generator(books_list_size)
            opc_submenu = None
            vector_cargado = True

            while opc_submenu not in range(3):
                m.print_submenu_opc1()
                opc_submenu = int(input('|--> Ingrese su opción: '))
                print('==' * 18)
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
                        while language_info not in range(1, 6):
                            m.language_menu()
                            language_info = int(input('IDIOMA: '))
                            leng_info = language_info - 1
                            leng_final = m.recorrer_idioma(leng_info)

                        price_info = float(input('PRECIO: '))

                        books[book_index] = Libro(isbn_info, title_info, gen_final, \
                                leng_final, price_info)

                elif opc_submenu == 2:
                    m.opcion1_automatica(books)

        elif opcion == 2:
            m.opcion2(books, vector_cargado)

        elif opcion == 3:
            gen_nom = ['Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía', \
                       'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']

            cant = m.contar_por_genero(books, gen_nom)
            m.opcion3(vector_cargado, cant)
            vec_cant = True

        elif opcion == 4:
            print('Búsqueda del mayor\n')
            idi_elegido = int(input('Ingrese el idioma de que quiere buscar el libro de mayor precio (1-5): '))
            m.opcion4(books, vector_cargado, idi_elegido)

        elif opcion == 5:
            if not vector_cargado:
                print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
            else:
                print('Búsqueda por ISBN\n')
                isbn_buscado = input('Ingrese el ISNB del libro que quiere buscar: ')
                m.opcion5(books, vector_cargado, isbn_buscado)

        elif opcion == 6:
            m.opcion6(books, vector_cargado, cant, vec_cant)

        elif opcion == 7:
            if not vector_cargado:
                print('Tiene que cargar la cantidad de libros primero (opcion 1)')

            else:
                breakpoint()
                request_isbn_list = []
                msj = 'Ingrese el ISBN [(e)xit para salir]: '
                msj_error = 'Ingrese ISBN válido [(e)xit para salir]: '
                request_isbn = ''

                while request_isbn != 'e':
                    request_isbn = input(msj)
                    isbn_valid_format, msj_format = m.validate_isbn_format(request_isbn)
                    isbn_valid_math_rel, msj_math = m.validate_isbn_math_relation(request_isbn)

                    while not isbn_valid_format or not isbn_valid_math_rel:
                        if not isbn_valid_format:
                            print('ERROR DE FORMATO: ', msj_format)

                        if not isbn_valid_math_rel:
                            print('ERROR MATEMÁTICO: ', msj_math)

                        request_isbn = input(msj_error)
                        if request_isbn == 'e':
                            break

                        isbn_valid_format, msj_format = m.validate_isbn_format(request_isbn)
                        isbn_valid_math_rel, msj_math = m.validate_isbn_math_relation(request_isbn)

                    if request_isbn != 'e':
                        request_isbn_list.append(request_isbn)


    print('¡Hasta luego!')


if __name__ == '__main__':
    main()
