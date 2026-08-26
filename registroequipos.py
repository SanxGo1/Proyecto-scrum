import json
from pathlib import Path

ARCHIVO = Path(__file__).parent / "equipos.json"


def pedir(msg, err="El valor no puede estar vacío."):
    while not (val := input(msg).strip()):
        print(err)
    return val


def elegir(msg, opciones):
    for k, v in opciones.items():
        print(f"{k}. {v}")
    while (opt := input(msg).strip()) not in opciones:
        print(f"Opción inválida ({', '.join(opciones)}).")
    return opciones[opt]


def cargar():
    if ARCHIVO.exists():
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al cargar: {e}")
    return []


def guardar(data):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar: {e}")


def registrar_equipo():
    print("\n--- Registro de equipo tecnológico ---")
    serie = pedir("Código de serie del equipo: ")

    tipos = {
        "1": "Computador",
        "2": "Monitor",
        "3": "Impresora",
        "4": "Teclado",
        "5": "Mouse",
        "6": "Portátil",
        "7": "Tablet",
        "8": "Otro",
    }
    tipo = elegir("Tipo (1-8): ", tipos)
    if tipo == "Otro":
        tipo = pedir("Especifique tipo: ")

    marcas = {
        "1": "Dell",
        "2": "HP",
        "3": "Lenovo",
        "4": "Apple",
        "5": "Samsung",
        "6": "Asus",
        "7": "Acer",
        "8": "Epson",
        "9": "Canon",
        "10": "Microsoft",
        "11": "Otra",
    }
    marca = elegir("Marca (1-11): ", marcas)
    if marca == "Otra":
        marca = pedir("Especifique marca: ")

    modelo = pedir("Modelo: ")
    estado = elegir(
        "Estado (1-3): ", {"1": "Bueno", "2": "Óptimo", "3": "Malo"}
    )

    equipo = {
        "codigo_serie": serie,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado,
    }
    guardar(cargar() + [equipo])



