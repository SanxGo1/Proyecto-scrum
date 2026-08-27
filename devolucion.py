import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
RUTA_ESTUDIANTES = BASE_DIR / "estudiantes.json"
RUTA_EQUIPOS = BASE_DIR / "equipos.json"
RUTA_PRESTAMOS = BASE_DIR / "prestamos.json"
RUTA_DEVOLUCIONES = BASE_DIR / "devoluciones.json"

def leer_json_absoluto(path_archivo, defecto):
    if path_archivo.exists():
        try:
            with open(path_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return datos if datos else defecto
        except Exception:
            try:
                with open(path_archivo, "r", encoding="latin-1") as f:
                    datos = json.load(f)
                    return datos if datos else defecto
            except Exception:
                return defecto
    return defecto

def guardar_json_absoluto(path_archivo, datos):
    with open(path_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def procesar_devolucion_computador():
    print("\n--- Módulo de Devolución de Computadores ---")
    
    estudiantes = leer_json_absoluto(RUTA_ESTUDIANTES, {})
    prestamos = leer_json_absoluto(RUTA_PRESTAMOS, {})
    equipos = leer_json_absoluto(RUTA_EQUIPOS, [])

    if not prestamos:
        print(f"❌ Error: El archivo de préstamos está vacío o no se encuentra en {RUTA_PRESTAMOS}.")
        return

    cedula_buscar = input("Ingrese el número de cédula del estudiante: ").strip()
    
    if not cedula_buscar:
        print("❌ Error: Debe ingresar un número de cédula válido.")
        return

    estudiante_existe = False
    if isinstance(estudiantes, dict):
        if cedula_buscar in estudiantes:
            estudiante_existe = True
        else:
            estudiante_existe = any(str(v.get("documento", "")) == cedula_buscar for v in estudiantes.values() if isinstance(v, dict))
    elif isinstance(estudiantes, list):
        estudiante_existe = any(str(e.get("documento", "")) == cedula_buscar for e in estudiantes if isinstance(e, dict))

    if not estudiante_existe:
        print(f"⚠️ Advertencia: La cédula '{cedula_buscar}' no aparece en 'estudiantes.json'. Verificando préstamos...")

    equipos_del_usuario = []
    if isinstance(prestamos, dict):
        for id_llave, info in prestamos.items():
            if isinstance(info, dict):
                id_p = str(info.get("id_prestamo") or id_llave)
                doc_estudiante = str(info.get("documento_estudiante") or info.get("documento") or "")
                estado_p = str(info.get("estado_prestamo") or info.get("estado") or "").lower()

                if doc_estudiante == cedula_buscar and estado_p in ["activo", "prestado"]:
                    equipos_del_usuario.append((id_p, info))

    if not equipos_del_usuario:
        print(f"❌ La cédula '{cedula_buscar}' no registra ningún préstamo activo.")
        return

    print(f"\n🔍 Préstamos activos encontrados para la cédula {cedula_buscar}:")
    for id_p, info in equipos_del_usuario:
        cod_eq = info.get('codigo_equipo') or info.get('codigo_serie') or 'N/A'
        fecha_p = info.get('fecha_prestamo') or 'N/A'
        print(f"   💻 ID Préstamo: {id_p} | Código Equipo: {cod_eq} | Fecha Préstamo: {fecha_p}")

    codigo_ingresado = input("\nIngrese el ID del préstamo a devolver (ej. PR-1): ").strip()
    
    codigo_encontrado = None
    info_prestamo = None
    for id_p, info in equipos_del_usuario:
        cod_eq = str(info.get("codigo_equipo") or info.get("codigo_serie") or "")
        if codigo_ingresado == id_p or codigo_ingresado == cod_eq:
            codigo_encontrado = id_p
            info_prestamo = info
            break

    if not codigo_encontrado:
        print("❌ El ID o código ingresado no coincide con los préstamos activos de este estudiante.")
        return

    confirmar = input(f"¿Confirma la devolución del préstamo '{codigo_encontrado}'? (s/n): ").strip().lower()
    if confirmar != 's':
        print("⚠️ Operación de devolución cancelada.")
        return

    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prestamos[codigo_encontrado]["estado_prestamo"] = "devuelto"
    prestamos[codigo_encontrado]["fecha_devolucion"] = fecha_hoy

    cod_equipo = str(info_prestamo.get("codigo_equipo") or info_prestamo.get("codigo_serie") or "")
    
    if isinstance(equipos, list):
        for eq in equipos:
            if isinstance(eq, dict):
                codigo_actual = str(eq.get("codigo_serie") or eq.get("codigo_equipo") or "")
                if codigo_actual == cod_equipo:
                    eq["disponibilidad"] = "disponible"
    elif isinstance(equipos, dict) and cod_equipo in equipos:
        equipos[cod_equipo]["disponibilidad"] = "disponible"

    try:
        guardar_json_absoluto(RUTA_PRESTAMOS, prestamos)
        guardar_json_absoluto(RUTA_EQUIPOS, equipos)

        devoluciones = leer_json_absoluto(RUTA_DEVOLUCIONES, [])
        if not isinstance(devoluciones, list):
            devoluciones = []

        devoluciones.append({
            "id_prestamo": codigo_encontrado,
            "documento_estudiante": cedula_buscar,
            "codigo_equipo": cod_equipo,
            "fecha_devolucion": fecha_hoy
        })

        guardar_json_absoluto(RUTA_DEVOLUCIONES, devoluciones)

        print(f"\n✅ ¡Devolución completada con éxito!")
        print(f"   - ID Préstamo: {codigo_encontrado}")
        print(f"   - Fecha de devolución: {fecha_hoy}")
    except Exception as e:
        print(f"❌ Error al guardar los cambios: {e}")