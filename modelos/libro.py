class Libro:
    """Representa un libro dentro del sistema de biblioteca."""

    def __init__(self, isbn, titulo, autor, cantidad):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    def __str__(self):
        return f"[{self.isbn}] {self.titulo} - {self.autor} (Cantidad: {self.cantidad})"