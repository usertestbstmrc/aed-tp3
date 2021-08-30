#!/usr/bin/python3

"""
Functions Module
+ All functions are documented
"""

# MÓDULO mic

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


def opcion1_automatica(v):
    """Genera libros de forma automatica"""
    v_range = len(v)

    for i in range(v_range):
        tit = ('Harry Potter', 'Percy Jackson', 'El Principito', 'Cien años de soledad',
                'El señor de los anillos', 'Un mundo feliz', 'Orgullo y prejuicio',
                'Crimen y castigo', 'Lolita', 'Ulises', 'El gran Gatsby', 'Mil soles espléndidos',
               'Alicia en el país de las maravillas', 'Rebelión en la granja', 'Los pilares de la tierra',
               'Guerra y paz', 'Memorias de una geisha', 'Frankenstein', 'Los viajes de Gulliver', 'La ladrona de libros')

        gen = ('Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía',
                'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros')

        lang_list = ('Español', 'Inglés', 'Francés', 'Italiano', 'Otros')
        titulo = random.choice(tit)
        genero = random.choice(gen)
        isbn = auto_gen_isbn()
        idioma = random.choice(lang_list)
        precio = round(random.uniform(0, 2000), 2)
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
        print('Datos de los libros: \n')
        mostrar_vector(v)


def opcion3(v, vec_car):
    gen_nom = ['Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía',\
            'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']

    if not vec_car:
        print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
    else:
        print('Conteo y género más popular\n')
        cant = contar_por_genero(v, gen_nom)
        mostrar_conteo(cant, gen_nom)
        mostrar_may(cant, gen_nom)


def opcion4(v, vector_cargado,idi_elegido):
    if vector_cargado == False:
        print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
    else:
        men_precio = 0
        may_precio = 0
        tit_mayor = ''
        for i in range(len(v)):
            pos = v[i].idioma
            posc = recorrer_idioma_inverso(pos)
            if posc == idi_elegido:
                if v[i].precio > men_precio:
                    may_precio = v[i].precio
                    tit_mayor = v[i].titulo

        if may_precio != 0:
            print('El libro de mayor precio es: ', tit_mayor)
            print('Este libro vale: $', may_precio)
        else:
            print('No se cargo ningun libro de ese idioma')


def opcion5(v, vector_cargado, isbn_buscado):
    if vector_cargado == False:
        print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
    else:
        encontrado = False
        format_valid, msj1 = validate_isbn_format(isbn_buscado)
        isbn_code_valid, msj2 = validate_isbn_math_relation(isbn_buscado)
        if format_valid:
            if isbn_code_valid:
                for i in range(len(v)):
                    if v[i].isbn == isbn_buscado:
                        encontrado = True
                        precio_total = v[i].precio + (10 * v[i].precio / 100)
                        v[i].precio = precio_total
                        print(v[i])

            else:
                print(msj2)
        else:
            print(msj1)
        if not encontrado:
            print('El libro no existe.')


def opcion6(v, vec_car, cant, vec_cant):
    if vec_car == False:
        print('Tiene que cargar la cantidad de libros primero (opcion 1): ')
    else:
        if vec_cant:
            mostrar_datos_may(v, cant)
        else:
            print('--' * 35)
            print('\t\tPrimero cagar opcion 3')
            print('--' * 35)


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
    print('==' * 18)


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


def contar_por_genero(v, gen_nom):
    n = len(v)
    cant = [0] * 10
    for i in range(n):
        pos = v[i].genero
        posc = recorrer_gen_inverso(gen_nom, pos)
        cant[posc] += 1
    return cant


def mostrar_conteo(cant, gen_nom):
    for i in range(len(cant)):
        if cant[i] > 0:
            print('*Cantidad de libros de género ', gen_nom[i], ':', cant[i])


def det_may(cant):
    n = len(cant)
    may = 0
    for i in range(n):
        if cant[i] > may:
            may = cant[i]
    return may


def mostrar_may(cant, gen_nom):
    may = det_may(cant)
    for i in range(len(cant)):
        if cant[i] == may:
            print('*El género más popular es: ', gen_nom[i])
            return


def recorrer_gen(genero_info):
    gen_nom = ['Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía',\
            'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']

    range_gender_list = len(gen_nom)
    index = 0

    for i in range(range_gender_list):
        if i == genero_info:
            index = i
            break
    
    return gen_nom[index]


def recorrer_idioma(idioma_info):
    idioma_nom = ['Español', 'Inglés', 'Francés', 'Italiano', 'Otros']
    range_idioma_list = len(idioma_nom)
    index = 0
    for i in range(range_idioma_list):
        if i == idioma_info:
            index = i
            break
    return idioma_nom[index]

def recorrer_idioma_inverso(pos):
    idioma_nom = ['0','Español', 'Inglés', 'Francés', 'Italiano', 'Otros']
    n = len(idioma_nom)
    c = 0
    for i in range(n):
        if pos == idioma_nom[i]:
            c = i
    return c

def recorrer_gen_inverso(gen_nom, pos):
    n = len(gen_nom)
    c = 0
    for i in range(n):
        if pos == gen_nom[i]:
            c = i
    return c


def auto_gen_isbn():
    """Return isbn string with valid math relation and format"""
    isbn_number = []

    while isbn_number == []:

        for i in range(10):
            dig = random.randint(0, 9)
            isbn_number.append(dig)

        pos = 10
        addition = 0
        for num in isbn_number:
            mult = pos * num
            addition += mult
            pos -= 1

        final_result = addition % 11

        if final_result != 0:
            isbn_number = []

        else:
            break

    string = str()
    for num in isbn_number:
        car = str(num)
        string += car

    string = list(string)

    string = string[0] + string[1] + '-' + string[2] + string[3] \
            + string[4] + string[5] + string[6] + '-' + string[7] \
            + string[8] + '-' + string[9]

    return string


def mostrar_datos_may(v, cant):
    gen_nom = ['Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía',\
            'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']
    #cant = contar_por_genero(v, gen_nom)
    may_n = det_may_nom(cant, gen_nom)
    ordenar_precio(v)
    for i in range(len(v)):
        if v[i].genero == may_n:
            print(v[i])


def det_may_nom(cant, gen_nom):
    n = len(cant)
    may_nom = 0
    may = 0
    for i in range(n):
        if cant[i] > may:
            may_nom = gen_nom[i]
            may = cant[i]
    return may_nom


def ordenar_precio(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i + 1, n):
            if v[i].precio < v[j].precio:
                v[i], v[j] = v[j], v[i]
