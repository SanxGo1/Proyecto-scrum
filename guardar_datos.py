import json
import os

def cargar_json(nombre_archivo, datos_por_defecto):
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            return datos_por_defecto
    else:
        guardar_json(nombre_archivo, datos_por_defecto)
        return datos_por_defecto

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)