import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modelos.libro import Libro
from dao.libro_dao import LibroDAO


class PruebasLibro(unittest.TestCase):

    def setUp(self):
        self.dao = LibroDAO()
        self.libro = Libro("1234567890", "Cien Años de Soledad", "G. García Márquez", 5)
        try:
            self.dao.registrar_libro(self.libro)
        except ValueError:
            pass

    def tearDown(self):
        try:
            self.dao.eliminar_libro(self.libro.isbn)
        except LookupError:
            pass

    def test_1_registrar_libro(self):
        nuevo = Libro("9876543210", "Rayuela", "Julio Cortázar", 3)
        resultado = self.dao.registrar_libro(nuevo)
        self.assertTrue(resultado)
        self.dao.eliminar_libro(nuevo.isbn)

    def test_2_buscar_libro(self):
        resultado = self.dao.buscar_libro(self.libro.isbn)
        self.assertEqual(resultado[1], "Cien Años de Soledad")

    def test_3_actualizar_libro(self):
        self.dao.actualizar_libro(self.libro.isbn, 10)
        resultado = self.dao.buscar_libro(self.libro.isbn)
        self.assertEqual(resultado[3], 10)

    def test_4_eliminar_libro(self):
        self.dao.eliminar_libro(self.libro.isbn)
        with self.assertRaises(LookupError):
            self.dao.buscar_libro(self.libro.isbn)

    def test_5_validar_isbn(self):
        self.assertTrue(self.dao.validar_isbn("1234567890"))
        with self.assertRaises(ValueError):
            self.dao.validar_isbn("abc123")


if __name__ == "__main__":
    unittest.main()