import sqlite3


def obtener_conexion():
    try:
        conexion = sqlite3.connect("biblioteca.db") 

        crear_tabla(conexion)
        return conexion
    except sqlite3.Error as error:
        raise ConnectionError(f"No fue posible conectar a la base de datos: {error}")


def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            cantidad INTEGER NOT NULL
        )
    """)
    conexion.commit()