from database.conexion import obtener_conexion


class LibroDAO:
    """Encargado exclusivamente de interactuar con la base de datos (patrón DAO)."""

    def validar_isbn(self, isbn):
        if not isbn:
            raise ValueError("El ISBN no puede estar vacío.")
        if not isbn.isdigit():
            raise ValueError("El ISBN solo debe contener números.")
        if len(isbn) not in (10, 13):
            raise ValueError("El ISBN debe tener 10 o 13 dígitos.")
        return True

    def registrar_libro(self, libro):
        self.validar_isbn(libro.isbn)
        if not libro.titulo or not libro.autor:
            raise ValueError("El título y el autor son obligatorios.")

        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO libros (isbn, titulo, autor, cantidad) VALUES (?, ?, ?, ?)",
                (libro.isbn, libro.titulo, libro.autor, libro.cantidad),
            )
            conexion.commit()
            return True
        finally:
            conexion.close()

    def buscar_libro(self, isbn):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM libros WHERE isbn = ?", (isbn,))
            resultado = cursor.fetchone()
            if resultado is None:
                raise LookupError(f"No existe un libro con ISBN {isbn}.")
            return resultado
        finally:
            conexion.close()

    def actualizar_libro(self, isbn, cantidad):
        self.buscar_libro(isbn)
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE libros SET cantidad = ? WHERE isbn = ?", (cantidad, isbn)
            )
            conexion.commit()
            return True
        finally:
            conexion.close()

    def eliminar_libro(self, isbn):
        self.buscar_libro(isbn)
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
            conexion.commit()
            return True
        finally:
            conexion.close()