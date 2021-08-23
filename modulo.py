#!/usr/bin/python3

# MÓDULO

# RO
def opcion1_manual():
    # ESTO LO ESTÁ HACIENDO MICA CREO
    pass

def opcion1_automatica():
    pass



def opcion2():
    pass


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
