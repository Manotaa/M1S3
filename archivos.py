import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """Save inventory to CSV"""
    if not inventario:
        print("Inventory is empty. Nothing to save.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventory saved in: {ruta}")

    except Exception as e:
        print("Error saving file:", e)


def cargar_csv(ruta):
    """Load inventory from CSV"""
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Invalid file format.")
                return []

            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"Loaded successfully. Invalid rows: {errores}")
        return inventario

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

    return []
