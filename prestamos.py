from datetime import datetime
from guardar_datos import cargar_json, guardar_json

RUTA_ESTUDIANTES = "estudiantes.json"
RUTA_EQUIPOS = "equipos.json"
RUTA_PRESTAMOS = "prestamos.json"

def registrar_prestamo(documento_estudiante, codigo_equipo):
    estudiantes = cargar_json(RUTA_ESTUDIANTES)
    equipos = cargar_json(RUTA_EQUIPOS)
    prestamos = cargar_json(RUTA_PRESTAMOS)

    doc_str = str(documento_estudiante)
    cod_str = str(codigo_equipo)

    if doc_str not in estudiantes:
        print(f"❌ Error: El estudiante con documento '{documento_estudiante}' no está registrado.")
        return False

    if cod_str not in equipos:
        print(f"❌ Error: El equipo con código '{codigo_equipo}' no existe.")
        return False

    equipo = equipos[cod_str]
    if equipo.get("estado", "").lower() != "disponible":
        print(f"❌ Error: El equipo '{codigo_equipo}' no se encuentra disponible. Estado actual: '{equipo.get('estado')}'.")
        return False

    id_prestamo = f"PR-{len(prestamos) + 1}"
    nuevo_prestamo = {
        "id_prestamo": id_prestamo,
        "documento_estudiante": doc_str,
        "codigo_equipo": cod_str,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "activo"
    }

    prestamos[id_prestamo] = nuevo_prestamo
    equipos[cod_str]["estado"] = "prestado"

    guardar_json(RUTA_PRESTAMOS, prestamos)
    guardar_json(RUTA_EQUIPOS, equipos)

    print(f"✅ Préstamo '{id_prestamo}' registrado con éxito para el equipo '{cod_str}'.")
    return True