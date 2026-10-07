# EJERCICIO 5 - SISTEMA DE CONSULTAS DE ÓRDENES DE REPARACIÓN

ordenes = [
    {"numero": 1, "cliente": "Juan", "equipo": "Notebook Lenovo", "falla": "No enciende", "estado": "En reparación", "costo": 50000},
    {"numero": 2, "cliente": "Maria", "equipo": "PC Dell", "falla": "Disco dañado", "estado": "Presupuesto", "costo": 70000},
    {"numero": 3, "cliente": "Pedro", "equipo": "Notebook HP", "falla": "Pantalla rota", "estado": "Reparado", "costo": 90000},
    {"numero": 4, "cliente": "Lucia", "equipo": "PC Exo", "falla": "No arranca", "estado": "En reparación", "costo": 45000},
    {"numero": 5, "cliente": "Sofia", "equipo": "Notebook Asus", "falla": "Teclado", "estado": "Reparado", "costo": 30000},
    {"numero": 6, "cliente": "Mateo", "equipo": "PC Lenovo", "falla": "Problema de RAM", "estado": "Presupuesto", "costo": 40000},
    {"numero": 7, "cliente": "Camila", "equipo": "Notebook Dell", "falla": "Batería", "estado": "En reparación", "costo": 35000},
    {"numero": 8, "cliente": "Tomás", "equipo": "PC HP", "falla": "Fuente dañada", "estado": "Reparado", "costo": 55000}
]


# Buscar una orden por número
def buscar_orden(numero):
    for orden in ordenes:
        if orden["numero"] == numero:
            return orden

    return None


# Filtrar por estado
def filtrar_por_estado(estado):
    encontrados = 0

    for orden in ordenes:
        if orden["estado"].lower() == estado.lower():
            print(orden)
            encontrados += 1

    if encontrados == 0:
        print("No existen órdenes con ese estado.")


# Filtrar por costo
def filtrar_por_costo(limite):
    encontrados = 0

    for orden in ordenes:
        if orden["costo"] <= limite:
            print(orden)
            encontrados += 1

    if encontrados == 0:
        print("No existen órdenes con ese costo o menor.")


# Menú principal
while True:

    print("\n===== MENÚ =====")
    print("1. Buscar orden por número")
    print("2. Filtrar órdenes por estado")
    print("3. Filtrar órdenes por costo")
    print("4. Mostrar todas las órdenes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Opción 1
    if opcion == "1":

        numero = int(input("Ingrese el número de orden: "))

        resultado = buscar_orden(numero)

        if resultado is not None:
            print("\nOrden encontrada:")
            print(resultado)
        else:
            print("No se encontró la orden.")

    # Opción 2
    elif opcion == "2":

        estado = input("Ingrese el estado: ")

        print("\n===== RESULTADOS =====")
        filtrar_por_estado(estado)

    # Opción 3
    elif opcion == "3":

        limite = float(input("Ingrese el costo máximo: "))

        print("\n===== RESULTADOS =====")
        filtrar_por_costo(limite)

    # Opción 4
    elif opcion == "4":

        print("\n===== TODAS LAS ÓRDENES =====")

        for orden in ordenes:
            print(orden)

    # Opción 5
    elif opcion == "5":

        print("Programa finalizado.")
        break

    # Opción inválida
    else:
        print("Opción incorrecta.")
        