"""
En este modulo se crea el tipo de dato Libro para luego ser instanciado.
- Se define el método (funcion constructora) __init__
- se define el método (función) __str__
"""

# REGISTRO
class Libro:
    """
    Tipo de dato.
    contiene los argumentos: isbn, titulo, genero, idioma, precio
    """

    def __init__(self, isbn: str = '', titulo: str = '', genero: str = '', idioma: str = '' \
            , precio: float = -1):
        """Función constructora"""
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


    def __str__(self) -> str:
        """Retorna una cadena de carateres str"""
        s_print = '|ISBN: {:<15} |Título: {:<25} |Género: {:<13} |Idioma: {:<11} |Precio: $ {:>7} '
        s_print = s_print.format(self.isbn, self.titulo, self.genero, self.idioma, self.precio)
        return s_print
