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

    def __init__(self, isbn: str = '', titulo: str = '', genero: int = -1, idioma: int = -1 \
            , precio: float = -1):
        """Función constructora"""
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


    def __str__(self) -> str:
        """Retorna una cadena de carateres str"""
        s = '|ISBN: ' + self.isbn
        s = '|Título: ' + self.titulo
        s += '|Género: ' + str(self.genero)
        s += '|Idioma: ' + str(self.genero)
        s += '|Precio: ' + str(self.precio)
        return s
