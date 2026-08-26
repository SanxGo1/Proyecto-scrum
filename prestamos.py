import json
import os
from datetime import datetime


def cargar_json(ruta_archivo):

    try:
        if not os.path.exists(ruta_archivo):

            return {} 
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} está corrupto. Verifica su formato.")
        return {}
    except Exception as e:
        print(f"Error inesperado al intentar leer {ruta_archivo}: {e}")
        return {}

def guardar_json(ruta_archivo, datos):

    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar la información en {ruta_archivo}: {e}")
def registrar_prestamo(documento_estudiante, codigo_equipo):
  
    estudiantes = cargar_json('estudiantes.json')
    equipos = cargar_json('equipos.json')
    prestamos = cargar_json('prestamos.json')

    if str(documento_estudiante) not in estudiantes:
        print(f"❌ Error: El estudiante con documento '{documento_estudiante}' no está registrado.")
        return False

 
    if str(codigo_equipo) not in equipos:
        print(f"❌ Error: El equipo con código '{codigo_equipo}' no existe en el inventario.")
        return False

   
    equipo = equipos[str(codigo_equipo)]
    if equipo.get('estado', '').lower() != 'disponible':
        print(f"❌ Error: El equipo '{codigo_equipo}' no puede ser prestado. Estado actual: {equipo.get('estado')}.")
        return False
    id_prestamo = f"PR-{len(prestamos) + 1}"
    
    nuevo_prestamo = {
        "id_prestamo": id_prestamo,
        "documento_estudiante": str(documento_estudiante),
        "codigo_equipo": str(codigo_equipo),
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "activo" 
    }
    
    prestamos[id_prestamo] = nuevo_prestamo

  
    equipos[str(codigo_equipo)]['estado'] = 'prestado'
    guardar_json('prestamos.json', prestamos)
    guardar_json('equipos.json', equipos)
    
    print(f"✅ ¡Éxito! Préstamo {id_prestamo} registrado correctamente.")
    return True
