# EJERCICIO 4 - DIAGNÓSTICO Y REPARACIÓN DE UN READ DEFECTUOSO

libros = [
    {"isbn": "1111", "titulo": "Python desde cero", "autor": "Juan Perez", "disponible": True},
    {"isbn": "2222", "titulo": "HTML y CSS", "autor": "Ana Gomez", "disponible": True},
    {"isbn": "3333", "titulo": "JavaScript básico", "autor": "Pedro Lopez", "disponible": False},
    {"isbn": "4444", "titulo": "Bases de datos", "autor": "Maria Diaz", "disponible": True},
    {"isbn": "5555", "titulo": "Introducción a redes", "autor": "Carlos Ruiz", "disponible": False}
]

# -------------------------------
# VERSIÓN INCORRECTA
# -------------------------------

print("===== VERSIÓN INCORRECTA =====")

isbn_buscado = input("Ingrese el ISBN a buscar: ")

for libro in libros:
    if libro["isbn"] == isbn_buscado:
        print("Libro encontrado:")
        print(libro)
    else:
        print("Libro no encontrado")


# -------------------------------
# VERSIÓN CORREGIDA
# -------------------------------

print("\n===== VERSIÓN CORREGIDA =====")

isbn_buscado = input("Ingrese nuevamente el ISBN a buscar: ")

encontrado = False

for libro in libros:

    if libro["isbn"] == isbn_buscado:
        print("\n===== LIBRO ENCONTRADO =====")
        print("ISBN:", libro["isbn"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Disponible:", libro["disponible"])

        encontrado = True

        # Detener la búsqueda
        break

# Mostrar el mensaje solamente si no se encontró
if encontrado == False:
    print("\nLibro no encontrado")
    