# menu_app.py

def agregar_compra(compras, total_gastado):
    compra = float(input("Ingrese el monto de la compra: "))
    compras.append(compra)
    total_gastado += compra
    print(f"Compra de {compra} agregada correctamente.")
    return compras, total_gastado

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra}")

def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            compras, total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
