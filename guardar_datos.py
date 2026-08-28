import json
import os
from pathlib import Path

def cargar_json(nombre_archivo, datos_por_defecto):
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            return datos_por_defecto
    else:
        guardar_json(nombre_archivo, datos_por_defecto)
        return datos_por_defecto

def guardar_json(nombre_archivo, datos):
    ruta = Path(nombre_archivo)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
