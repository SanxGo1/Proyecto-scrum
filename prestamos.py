import json
from pathlib import Path
from datetime import datetime
from guardar_datos import guardar_json

BASE_DIR = Path(__file__).resolve().parent
RUTA_ESTUDIANTES = str(BASE_DIR / "estudiantes.json")
RUTA_EQUIPOS = str(BASE_DIR / "equipos.json")
RUTA_PRESTAMOS = str(BASE_DIR / "prestamos.json")

def leer_json_seguro(ruta, defecto):
    ruta_path = Path(ruta)
    if ruta_path.exists():
        try:
            with open(ruta_path, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return datos if datos else defecto
        except:
            try:
                with open(ruta_path, "r") as f:
                    datos = json.load(f)
                    return datos if datos else defecto
            except:
                pass
    return defecto


def registrar_prestamo():
    print("\n--- Registro de Nuevo Préstamo ---")
    
    estudiantes = leer_json_seguro(RUTA_ESTUDIANTES, {})
    equipos = leer_json_seguro(RUTA_EQUIPOS, []) 
    prestamos = leer_json_seguro(RUTA_PRESTAMOS, {})

    doc_estudiante = input("Ingrese el documento del estudiante: ").strip()
    if doc_estudiante not in estudiantes:
        print(f"❌ Error: El estudiante con documento '{doc_estudiante}' no está registrado.")
        return False
    
    nombre_est = estudiantes[doc_estudiante].get("nombre", "Desconocido")
    print(f"👤 Estudiante validado: {nombre_est}\n")

    print("\n--- Catálogo de Equipos ---")
    if not equipos:
        print("⚠️ No hay equipos registrados en el sistema.")
        return False
        
    for idx, eq in enumerate(equipos, start=1):
        if isinstance(eq, dict):
            tipo = eq.get("tipo", "N/A")
            marca = eq.get("marca", "N/A")
            modelo = eq.get("modelo", "N/A")
            serie = eq.get("codigo_serie", "N/A")
            estado_fisico = eq.get("estado", "N/A")
            disponibilidad = eq.get("disponibilidad", "disponible").upper()
            indicador = "🟢" if disponibilidad == "DISPONIBLE" else "🔴"
            
            print(f"{idx}. {indicador} [{disponibilidad}] | Serie: {serie} | {tipo} {marca} {modelo} | Físico: {estado_fisico}")
    print("---------------------------\n")

    cod_equipo = input("Ingrese el código de serie del equipo a prestar: ").strip()
    
    equipo_encontrado = None
    indice_equipo = -1
    for i, eq in enumerate(equipos):
        if eq.get("codigo_serie") == cod_equipo:
            equipo_encontrado = eq
            indice_equipo = i
            break
            
    if not equipo_encontrado:
        print(f"❌ Error: El equipo '{cod_equipo}' no existe en el sistema.")
        return False

    estado_fisico = equipo_encontrado.get("estado", "").lower()
    disponibilidad = equipo_encontrado.get("disponibilidad", "disponible").lower() 

    if disponibilidad == "prestado":
        print(f"❌ Error: El equipo '{cod_equipo}' ya se encuentra prestado actualmente.")
        return False
    elif estado_fisico == "malo":
        print(f"❌ Error: El equipo '{cod_equipo}' se encuentra en mal estado físico y no se puede prestar.")
        return False

    siguiente_id = 1
    if prestamos and isinstance(prestamos, dict):
        for k in prestamos.keys():
            if str(k).startswith("PR-"):
                try:
                    numero = int(str(k).split("-")[1])
                    if numero >= siguiente_id:
                        siguiente_id = numero + 1
                except (ValueError, IndexError):
                    continue
                    
    id_prestamo = f"PR-{siguiente_id}"

    prestamos[id_prestamo] = {
        "id_prestamo": id_prestamo,
        "documento_estudiante": doc_estudiante,
        "codigo_equipo": cod_equipo,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado_prestamo": "activo"
    }

    equipos[indice_equipo]["disponibilidad"] = "prestado"

    guardar_json(RUTA_PRESTAMOS, prestamos)
    guardar_json(RUTA_EQUIPOS, equipos)

    print(f"\n✅ Préstamo '{id_prestamo}' registrado con éxito.")
    print(f"   💻 Equipo: {equipo_encontrado.get('tipo')} {equipo_encontrado.get('marca')} -> Prestado a: {nombre_est}")
    return True