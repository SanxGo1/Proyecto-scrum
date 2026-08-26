
import os 
import json
from pathlib import Path


ARCHIVO_EQUIPOS = Path(__file__).with_name("equipos.json")


def guardar_equipos(equipos, archivo=ARCHIVO_EQUIPOS):
	
	with Path(archivo).open("w", encoding="utf-8") as fichero:
		json.dump(equipos, fichero, ensure_ascii=False, indent=4)


def cargar_equipos(archivo=ARCHIVO_EQUIPOS):
	ruta = Path(archivo)
	if not ruta.exists():
		return []

	with ruta.open("r", encoding="utf-8") as fichero:
		return json.load(fichero)
