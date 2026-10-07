# EJERCICIO 2 - BUSCADOR FLEXIBLE DE REPUESTOS

repuestos = [
    {"codigo": "R001", "descripcion": "SSD Kingston 480 GB", "categoria": "Almacenamiento", "marca": "Kingston", "precio": 45000, "stock": 5},
    {"codigo": "R002", "descripcion": "SSD Crucial 1 TB", "categoria": "Almacenamiento", "marca": "Crucial", "precio": 70000, "stock": 0},
    {"codigo": "R003", "descripcion": "Memoria RAM 8 GB DDR4", "categoria": "Memoria", "marca": "Kingston", "precio": 30000, "stock": 8},
    {"codigo": "R004", "descripcion": "Memoria RAM 16 GB DDR4", "categoria": "Memoria", "marca": "Corsair", "precio": 55000, "stock": 3},
    {"codigo": "R005", "descripcion": "Fuente 600W", "categoria": "Fuente", "marca": "Thermaltake", "precio": 60000, "stock": 2},
    {"codigo": "R006", "descripcion": "Placa de video RTX 3060", "categoria": "Video", "marca": "Asus", "precio": 250000, "stock": 0},
    {"codigo": "R007", "descripcion": "Teclado mecánico", "categoria": "Periféricos", "marca": "Redragon", "precio": 50000, "stock": 4},
    {"codigo": "R008", "descripcion": "Mouse inalámbrico", "categoria": "Periféricos", "marca": "Logitech", "precio": 25000, "stock": 6}
]

busqueda = input("Ingrese una descripción o parte de ella: ").lower()

coincidencias = 0
disponibles = 0

print("\n===== RESULTADOS =====")

for repuesto in repuestos:
    descripcion = repuesto["descripcion"].lower()

    # Buscar una parte de la descripción
    if busqueda in descripcion:
        coincidencias += 1

        print("\nCódigo:", repuesto["codigo"])
        print("Descripción:", repuesto["descripcion"])
        print("Categoría:", repuesto["categoria"])
        print("Marca:", repuesto["marca"])
        print("Precio:", repuesto["precio"])
        print("Stock:", repuesto["stock"])

        # Comprobar si hay stock
        if repuesto["stock"] > 0:
            print("Estado: Disponible")
            disponibles += 1
        else:
            print("Estado: Sin stock")

print("\nCantidad total de coincidencias:", coincidencias)
print("Cantidad disponible:", disponibles)

if coincidencias == 0:
    print("La búsqueda no produjo resultados.")
    