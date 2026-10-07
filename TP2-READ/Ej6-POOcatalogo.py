# EJERCICIO 6 - POO: CATÁLOGO DE DISPOSITIVOS DE RED


# Clase DispositivoRed
class DispositivoRed:

    def __init__(self, codigo, tipo, marca, velocidad_mbps, precio, stock):
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.velocidad_mbps = velocidad_mbps
        self.precio = precio
        self.stock = stock

    # Mostrar los datos del dispositivo
    def mostrar_datos(self):
        print("Código:", self.codigo)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Velocidad:", self.velocidad_mbps, "Mbps")
        print("Precio:", self.precio)
        print("Stock:", self.stock)

    # Comprobar si hay stock
    def hay_stock(self):
        return self.stock > 0


# Crear los dispositivos
dispositivos = [
    DispositivoRed("D001", "Router", "TP-Link", 1000, 85000, 5),
    DispositivoRed("D002", "Switch", "Cisco", 1000, 150000, 2),
    DispositivoRed("D003", "Access Point", "Ubiquiti", 1200, 180000, 3),
    DispositivoRed("D004", "Router", "MikroTik", 2000, 220000, 0),
    DispositivoRed("D005", "Switch", "TP-Link", 1000, 70000, 6),
    DispositivoRed("D006", "Access Point", "TP-Link", 300, 50000, 4)
]


# Buscar dispositivos por velocidad mínima y con stock
def buscar_por_velocidad(velocidad_minima):

    encontrados = 0

    for dispositivo in dispositivos:

        if dispositivo.velocidad_mbps >= velocidad_minima and dispositivo.hay_stock():
            dispositivo.mostrar_datos()
            print()
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron dispositivos con esa velocidad y con stock.")


# Buscar un dispositivo por código
def buscar_por_codigo(codigo):

    for dispositivo in dispositivos:

        if dispositivo.codigo.lower() == codigo.lower():
            return dispositivo

    return None


# Consultar velocidad mínima
velocidad = int(input("Ingrese la velocidad mínima en Mbps: "))

print("\n===== DISPOSITIVOS POR VELOCIDAD =====")

buscar_por_velocidad(velocidad)


# Consultar por código
codigo = input("\nIngrese el código del dispositivo a buscar: ")

resultado = buscar_por_codigo(codigo)

if resultado is not None:
    print("\n===== DISPOSITIVO ENCONTRADO =====")
    resultado.mostrar_datos()
else:
    print("No se encontró el dispositivo.")


# Consultar presupuesto
presupuesto = float(input("\nIngrese el presupuesto máximo: "))

print("\n===== DISPOSITIVOS QUE PUEDEN COMPRARSE =====")

encontrados = 0

for dispositivo in dispositivos:

    if dispositivo.hay_stock() and dispositivo.precio <= presupuesto:
        dispositivo.mostrar_datos()
        print()
        encontrados += 1

if encontrados == 0:
    print("No hay dispositivos con stock que entren en el presupuesto.")