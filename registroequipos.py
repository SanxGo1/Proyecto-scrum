from pathlib import Path
from guardar_datos import cargar_json, guardar_json

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
    estado = elegir("Estado (1-3): ", {"1": "Bueno", "2": "Óptimo", "3": "Malo"})

    equipos = cargar_json(str(ARCHIVO), [])

    equipo = {
        "codigo_serie": serie,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado,
    }
    
    equipos.append(equipo)
    guardar_json(str(ARCHIVO), equipos)
    print("✅ Equipo registrado y guardado exitosamente.")



