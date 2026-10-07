# EJERCICIO 1 - CONTROL DEL LABORATORIO

equipos = [
    {"inventario": 1001, "tipo": "Notebook", "marca": "Lenovo", "estado": "Disponible", "anio": 2022},
    {"inventario": 1002, "tipo": "PC", "marca": "Dell", "estado": "En reparación", "anio": 2021},
    {"inventario": 1003, "tipo": "Notebook", "marca": "HP", "estado": "Disponible", "anio": 2019},
    {"inventario": 1004, "tipo": "PC", "marca": "Exo", "estado": "Baja", "anio": 2018},
    {"inventario": 1005, "tipo": "All-in-One", "marca": "Lenovo", "estado": "Disponible", "anio": 2023},
    {"inventario": 1006, "tipo": "Notebook", "marca": "Asus", "estado": "Disponible", "anio": 2020},
    {"inventario": 1007, "tipo": "PC", "marca": "Dell", "estado": "En reparación", "anio": 2024},
    {"inventario": 1008, "tipo": "Notebook", "marca": "Acer", "estado": "Disponible", "anio": 2021}
]

anio_minimo = int(input("Ingrese el año mínimo: "))

cantidad = 0

print("\nEquipos disponibles desde el año indicado:")
print("-----------------------------------------")

# Único recorrido de la lista
for equipo in equipos:
    if equipo["estado"] == "Disponible" and equipo["anio"] >= anio_minimo:
        print(equipo)
        cantidad += 1

print("\nCantidad de equipos que cumplen las condiciones:", cantidad)

if cantidad == 0:
    print("No existe ningún equipo disponible que cumpla con el año solicitado.")
    