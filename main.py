from modelos.libro import Libro
from dao.libro_dao import LibroDAO


def menu():
    dao = LibroDAO()

    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Registrar libro")
        print("2. Buscar libro")
        print("3. Actualizar cantidad")
        print("4. Eliminar libro")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                isbn = input("ISBN: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                cantidad = int(input("Cantidad: "))
                libro = Libro(isbn, titulo, autor, cantidad)
                dao.registrar_libro(libro)
                print("Libro registrado correctamente.")

            elif opcion == "2":
                isbn = input("ISBN a buscar: ")
                resultado = dao.buscar_libro(isbn)
                print("Libro encontrado:", resultado)

            elif opcion == "3":
                isbn = input("ISBN a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                dao.actualizar_libro(isbn, cantidad)
                print("Cantidad actualizada correctamente.")

            elif opcion == "4":
                isbn = input("ISBN a eliminar: ")
                dao.eliminar_libro(isbn)
                print("Libro eliminado correctamente.")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except ValueError as error:
            print(f"Dato inválido: {error}")
        except LookupError as error:
            print(f"Registro no encontrado: {error}")
        except ConnectionError as error:
            print(f"Error de conexión a la base de datos: {error}")
        except ZeroDivisionError:
            print("No es posible dividir entre cero.")
        finally:
            print("Operación finalizada.")


if __name__ == "__main__":
    menu()