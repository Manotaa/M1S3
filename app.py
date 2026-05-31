from servicios import *
from archivos import *

inventario = []

def menu():
    print("\n===== INVENTORY SYSTEM =====")
    print("1. Add")
    print("2. Show")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")


def main():
    global inventario

    opcion = ""

    while opcion != "9":
        menu()
        opcion = input("Choose option: ").strip()

        try:
            if opcion == "1":
                nombre = input("Name: ")
                precio = float(input("Price: "))
                cantidad = int(input("Quantity: "))
                agregar_producto(inventario, nombre, precio, cantidad)

            elif opcion == "2":
                mostrar_inventario(inventario)

            elif opcion == "3":
                nombre = input("Name: ")
                print(buscar_producto(inventario, nombre))

            elif opcion == "4":
                nombre = input("Name: ")
                precio = input("New price: ")
                cantidad = input("New quantity: ")

                actualizar_producto(
                    inventario,
                    nombre,
                    float(precio) if precio else None,
                    int(cantidad) if cantidad else None
                )

            elif opcion == "5":
                nombre = input("Name: ")
                eliminar_producto(inventario, nombre)

            elif opcion == "6":
                stats = calcular_estadisticas(inventario)
                if stats:
                    print(stats)

            elif opcion == "7":
                ruta = input("File path: ")
                guardar_csv(inventario, ruta)

            elif opcion == "8":
                ruta = input("File path: ")
                nuevo = cargar_csv(ruta)

                if nuevo:
                    resp = input("Overwrite? (S/N): ").lower()
                    if resp == "s":
                        inventario = nuevo
                    else:
                        inventario.extend(nuevo)

            elif opcion == "9":
                print("Goodbye")

            else:
                print("Invalid option")

        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
