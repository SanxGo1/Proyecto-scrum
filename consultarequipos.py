import json
from pathlib import Path

ARCHIVO_EQUIPOS = Path(__file__).parent / "equipos.json"


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
            print(
                f"{idx}. [{eq.get('tipo', 'N/A')}] {eq.get('marca', '')} {eq.get('modelo', '')} "
                f"| Serie: {eq.get('codigo_serie', 'N/A')} | Estado: {eq.get('estado', 'N/A')}"
            )
        else:
            print(f"{idx}. {eq}")


if __name__ == "__main__":
    consultar_equipos()