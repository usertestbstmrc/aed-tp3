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


def validate_isbn_math_relation(isbn):
    """Return boolean value True if isbn code math relation is valid"""
    isbn_code_valid = False
    isbn_only_numbers = []

    for character in isbn:
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

    return isbn_code_valid


def opcion1_automatica(v):
    for i in range(len(v)):
        tit = ('Harry Potter', 'Percy Jackson', 'El Principito')
        isb = ('44--5', '5555--69', '75314--8') #despues cambiar
        isbn = random.choice(tit)
        titulo = random.choice(isb)
        idioma = random.randint(0, 10)
        genero = random.randint(0, 10)
        precio = round(random.uniform(0, 100), 2)
        v[i] = Libro(isbn, titulo, genero, idioma, precio)
    print()
    print('\t\tVECTOR CARGADO')
    print()


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])

def opcion2(v):
    if v[0] is None:
        print('Tiene que cargar el libro primero (opcion 1): ')
    else:
        mostrar_vector(v)



def opcion3():
    pass


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
