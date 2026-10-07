# EJERCICIO 3 - CONSULTA DE ALUMNOS

alumnos = [
    {"nombre": "Lucía", "curso": "4°4°", "promedio": 8.5, "trabajos": 9},
    {"nombre": "Mateo", "curso": "4°4°", "promedio": 7.2, "trabajos": 8},
    {"nombre": "Sofía", "curso": "4°4°", "promedio": 9.3, "trabajos": 10},
    {"nombre": "Juan", "curso": "4°4°", "promedio": 6.5, "trabajos": 7},
    {"nombre": "Martina", "curso": "4°4°", "promedio": 8.9, "trabajos": 9},
    {"nombre": "Tomás", "curso": "4°4°", "promedio": 5.8, "trabajos": 6},
    {"nombre": "Valentina", "curso": "4°4°", "promedio": 7.8, "trabajos": 8},
    {"nombre": "Nicolás", "curso": "4°4°", "promedio": 9.0, "trabajos": 10},
    {"nombre": "Camila", "curso": "4°4°", "promedio": 6.9, "trabajos": 7},
    {"nombre": "Bruno", "curso": "4°4°", "promedio": 8.1, "trabajos": 9}
]

promedio_minimo = float(input("Ingrese el promedio mínimo requerido: "))
trabajos_minimos = int(input("Ingrese la cantidad mínima de trabajos entregados: "))

cumplen = 0
no_cumplen = 0

# Variables auxiliares
mejor_promedio = -1
mejor_alumno = None

print("\n===== ALUMNOS QUE CUMPLEN =====")

for alumno in alumnos:

    if alumno["promedio"] >= promedio_minimo and alumno["trabajos"] >= trabajos_minimos:
        print("Nombre:", alumno["nombre"])
        print("Promedio:", alumno["promedio"])
        print("Trabajos entregados:", alumno["trabajos"])
        print()

        cumplen += 1

        # Buscar el promedio más alto sin usar max()
        if alumno["promedio"] > mejor_promedio:
            mejor_promedio = alumno["promedio"]
            mejor_alumno = alumno["nombre"]

    else:
        no_cumplen += 1

print("Cantidad que cumple:", cumplen)
print("Cantidad que no cumple:", no_cumplen)

if cumplen > 0:
    print("\n===== MEJOR PROMEDIO =====")
    print("Nombre:", mejor_alumno)
    print("Promedio:", mejor_promedio)
else:
    print("Ningún alumno cumple con las condiciones.")