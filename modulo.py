#!/usr/bin/python3

"""
Functions Module
+ All functions are documented
"""

# MÓDULO

import random
from registro import Libro

def list_generator(size: int) -> list:
    """Create list with 'n' slots"""
    libros = size * [None]

    return libros


def gender_menu():
    """Print gender menu"""
    gen_menu = '\nGÉNERO' + '\n|-> 0. Autoayuda' + '\n|-> 1. Arte' + '\n|-> 2. Ficción' \
            + '\n|-> 3. Computación' + '\n|-> 4. Economía'+ '\n|-> 5. Escolar' \
            + '\n|-> 6. Sociedad' + '\n|-> 7. Gastronomía' + '\n|-> 8. Infantil' \
            + '\n|-> 9. Otros'

    print(gen_menu)

def language_menu():
    """Print Languaje menu"""
    lan_menu = '\nIDIOMA' + '\n|-> 1. Español' + '\n|-> 2. Inglés' + '\n|-> 3. Francés' \
            + '\n|-> 4. Italiano' + '\n|-> 5. Otros'

    print(lan_menu)


def validate_isbn_format(isbn_code: str):
    """Return boolean value True if isbn format is valid"""
    format_valid = False
    isbn = list(isbn_code)
    msj = ''

    if len(isbn) == 13:

        isbn_numbers = []
        isbn_separator = []
        index = 0
        isbn_characters = []

        for character in isbn:

            if character in '0123456789':
                isbn_numbers.append(character)

            elif character not in '0123456789':
                isbn_characters.append(character)

                if character == '-':
                    isbn_separator.append(character)

                    if index > 0:
                        if isbn[index - 1] not in '0123456789':
                            msj = 'Se ingresaron dos separadores juntos'
                            break
                else:
                    msj = 'Se ingresó un caracter inválido'
                    break

            index += 1

        if len(isbn_numbers) < 10:
            msj = 'Faltan dígitos'

        if len(isbn_separator) != 3:
            msj = 'No son 4 grupos de números.'

            if len(isbn_separator) < 3:
                diff = 3 - len(isbn_separator)
                msj += ' Faltan ' + str(diff) + ' separadores'
            else:
                diff = len(isbn_separator) - 3
                msj += ' Hay ' + str(diff) + ' separador sobrante'

        if msj == '':
            format_valid = True

    elif len(isbn) < 13:
        msj = 'Faltan caracteres'

    else:
        msj = 'Se excede la cantidad de carácteres'

    return format_valid, msj


def validate_isbn_math_relation(isbn_code: str):
    """Return boolean value True if isbn code math relation is valid"""
    isbn_code_valid = False
    isbn_only_numbers = []
    msj = ''

    for character in isbn_code:
        if character in '0123456789':
            char_parse_int = int(character)
            isbn_only_numbers.append(char_parse_int)
        else:
            pass

    pos = 10
    addition = 0
    for num in isbn_only_numbers:
        mult = pos * num
        addition += mult
        pos -= 1

    final_result = addition % 11

    if final_result == 0:
        isbn_code_valid = True

    if not isbn_code_valid:
        msj = 'No se cumple la relación matemática'

    return isbn_code_valid, msj

##### xd
def opcion1_automatica(v):
    for i in range(len(v)):
        tit = ('Harry Potter', 'Percy Jackson', 'El Principito')
        isb = ('0-7645-2641-3', '0-7645-2641-3', '0-7645-2641-3') #despues cambiar
        isbn = random.choice(tit)
        titulo = random.choice(isb)
        idioma = random.randint(1, 5)
        genero = random.randint(0, 9)
        precio = round(random.uniform(0, 10000000), 2)
        v[i] = Libro(isbn, titulo, genero, idioma, precio)
    print()
    print('\t\tVECTOR CARGADO')
    print()


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])

def opcion2(v, vec_car):
    if vec_car == False:
        print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
    else:
        mostrar_vector(v)



def opcion3(v, vec_car, gen_nom):
    if vec_car == False:
        print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
    else:
        cant = contar_por_genero(v)
        mostrar_conteo(cant, gen_nom)
        mostrar_may(cant, gen_nom)


def opcion4():
    pass


def opcion5():
    pass


def opcion6():
    pass


def opcion7():
    pass


def mostrar_opciones():
    print('==' * 18)
    print('MENU DE OPCIONES')
    print('1. Generación y Carga de libros')
    print('2. Mostrar datos de libros')
    print('3. Conteo y género más popular:')
    print('4. Búsqueda del mayor:')
    print('5. Búsqueda por ISBN:')
    print('6. Consulta de un género:')
    print('7. Consulta de precio por grupo:')
    print('8. Salir')


def print_submenu_opc1():
    """Print in console submenu option 1"""

    sub_m = '==' * 18 + '\n|--> 1. Carga Manual' +  '\n|' \
            + '\n|--> 2. Generación Automática' + '\n|'

    print(sub_m)


def validar_carga(inf, mensaje):
    n = int(input(mensaje))
    while n <= inf:
        n = int(input('¡ERROR!' + mensaje))
    return n


def contar_por_genero(v):
    n = len(v)
    cant = [0] * 10
    for i in range(n):
        pos = v[i].genero
        cant[pos] += 1
    return cant


def mostrar_conteo(cant, gen_nom):
    for i in range(len(cant)):
        if cant[i] > 0:
            print('Cantidad de libros de género ', gen_nom[i], ':', cant[i])


def det_may(cant):
    n = len(cant)
    may = None
    for i in range(n-1):
        for j in range(i + 1, n):
            if cant[i] > 0:
                if cant[i] > cant[j]:
                    may = cant[i]
                elif cant[j] > cant[i]:
                    may = cant[j]
                else:
                    may = cant[i]
    return may


def mostrar_may(cant, gen_nom):
    may = det_may(cant)
    for i in range(len(cant)):
        if cant[i] == may:
            print('El género más popular es:  ', gen_nom[i])
            return
