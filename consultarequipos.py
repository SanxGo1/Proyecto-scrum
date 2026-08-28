import json
from pathlib import Path

# Ruta actualizada a la carpeta datos
ARCHIVO_EQUIPOS = Path(__file__).parent / "datos" / "equipos.json"

def consultar_equipos(ruta=ARCHIVO_EQUIPOS):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            equipos = json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
        return
    except json.JSONDecodeError:
        print("El archivo JSON no tiene un formato válido.")
        return

    if not equipos:
        print("No hay equipos registrados.")
        return

    print("\n--- Equipos Tecnológicos Registrados ---")
    for idx, eq in enumerate(equipos, start=1):
        if isinstance(eq, dict):
            disponibilidad = eq.get("disponibilidad") or eq.get("disponible")
            
            if disponibilidad is None:
                estado = eq.get("estado", "").lower()
                disponibilidad = "Disponible" if estado == "bueno" or estado == "disponible" else "No Disponible"

            print(
                f"{idx}. [{eq.get('tipo', 'N/A')}] {eq.get('marca', '')} {eq.get('modelo', '')} "
                f"| Serie: {eq.get('codigo_serie', 'N/A')} "
                f"| Estado: {eq.get('estado', 'N/A')} "
                f"| Disponibilidad: {disponibilidad}"
            )
        else:
            print(f"{idx}. {eq}")

if __name__ == "__main__":
    consultar_equipos()
