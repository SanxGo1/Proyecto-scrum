from datetime import datetime
from guardar_datos import cargar_json, guardar_json

RUTA_ESTUDIANTES = "estudiantes.json"
RUTA_EQUIPOS = "equipos.json"
RUTA_PRESTAMOS = "prestamos.json"

def registrar_prestamo():
    print("\n--- Registro de Nuevo Préstamo ---")
    
    estudiantes = cargar_json(RUTA_ESTUDIANTES, {})
    equipos = cargar_json(RUTA_EQUIPOS, []) 
    prestamos = cargar_json(RUTA_PRESTAMOS, {})

   
    doc_estudiante = input("Ingrese el documento del estudiante: ").strip()
    if doc_estudiante not in estudiantes:
        print(f"❌ Error: El estudiante con documento '{doc_estudiante}' no está registrado.")
        return False
    
    nombre_est = estudiantes[doc_estudiante].get("nombre", "Desconocido")
    print(f"👤 Estudiante validado: {nombre_est}")


    cod_equipo = input("Ingrese el código de serie del equipo: ").strip()
    
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

    estado_actual = equipo_encontrado.get("estado", "").lower()
    if estado_actual == "prestado":
        print(f"❌ Error: El equipo '{cod_equipo}' ya se encuentra prestado.")
        return False
    elif estado_actual == "malo":
        print(f"❌ Error: El equipo '{cod_equipo}' está en mal estado y no puede prestarse.")
        return False

 
    id_prestamo = f"PR-{len(prestamos) + 1}"
    prestamos[id_prestamo] = {
        "id_prestamo": id_prestamo,
        "documento_estudiante": doc_estudiante,
        "codigo_equipo": cod_equipo,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "activo"
    }

    equipos[indice_equipo]["estado"] = "prestado"

    guardar_json(RUTA_PRESTAMOS, prestamos)
    guardar_json(RUTA_EQUIPOS, equipos)

    print(f"\n✅ Préstamo '{id_prestamo}' registrado con éxito.")
    print(f"   💻 Equipo: {equipo_encontrado.get('tipo')} {equipo_encontrado.get('marca')} -> Prestado a: {nombre_est}")
    return True