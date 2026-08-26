<<<<<<< HEAD

from datetime import datetime
import json
import os
=======
import os
from datetime import datetime
from guardar_datos import cargar_json, guardar_json
>>>>>>> 2c3b56e92cc69e7b0f462fb69046e189b81e821f

def procesar_devolucion_computador(archivo="prestamos.json"):
    print("\n--- Módulo de Devolución de Computadores ---")
    
    prestamos = cargar_json(archivo, {})
    if not prestamos:
        print(f"❌ Error: El archivo '{archivo}' está vacío o no existe.")
        return

    cedula_buscar = input("Ingrese el número de cédula del estudiante: ").strip()
    
    if not cedula_buscar:
        print("❌ Error: Debe ingresar un número de cédula válido.")
        return

    equipos_del_usuario = []
    for codigo_pc, info in prestamos.items():
        if isinstance(info, dict) and info.get("estado") == "activo" and str(info.get("documento_estudiante")) == cedula_buscar:
            equipos_del_usuario.append((codigo_pc, info))

    if not equipos_del_usuario:
        print(f"❌ La cédula '{cedula_buscar}' no registra ningún equipo en estado 'activo'.")
        return

    print(f"\n🔍 ¡Equipos encontrados para el documento {cedula_buscar}:")
    for codigo_pc, info in equipos_del_usuario:
        print(f"   💻 ID Préstamo: {codigo_pc} | Equipo: {info.get('codigo_equipo')} | Fecha: {info.get('fecha_prestamo')}")

    codigo_ingresado = input("\nIngrese el ID del préstamo o código del equipo a devolver: ").strip()
    
    codigo_encontrado = None
    for codigo_pc, info in equipos_del_usuario:
        if codigo_ingresado in codigo_pc or codigo_ingresado in str(info.get('codigo_equipo')):
            codigo_encontrado = codigo_pc
            break

    if not codigo_encontrado:
        print("❌ El código ingresado no coincide con los préstamos activos de este estudiante.")
        return

    confirmar = input(f"¿Confirma que desea procesar la devolución? (s/n): ").strip().lower()
    if confirmar != 's':
        print("⚠️ Operación de devolución cancelada.")
        return

    prestamos[codigo_encontrado]["estado"] = "devuelto"
    prestamos[codigo_encontrado]["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

<<<<<<< HEAD
    prestamos[codigo_encontrado] = {
        "estado": "disponible",
        "documento": None,
        "nombre": None,
        "correo": None,
        "programa_academico": None,
        "fecha_prestamo": None,
        "fecha_devolucion": fecha_devolucion_hoy
    }

    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(prestamos, f, indent=4, ensure_ascii=False)

        devoluciones = []
        try:
            with open("devolucion.json", "r", encoding="utf-8") as f:
                contenido_devoluciones = f.read().strip()
                if contenido_devoluciones:
                    devoluciones = json.loads(contenido_devoluciones)
        except (FileNotFoundError, json.JSONDecodeError, IOError):
            devoluciones = []

        if not isinstance(devoluciones, list):
            devoluciones = []

        devoluciones.append({
            "equipo": codigo_encontrado,
            "documento": cedula_buscar,
            "fecha_devolucion": fecha_devolucion_hoy
        })

        with open("devolucion.json", "w", encoding="utf-8") as f:
            json.dump(devoluciones, f, indent=4, ensure_ascii=False)

        print(f"\n✅ ¡Devolución completada con éxito!")
        print(f"   - Equipo: {codigo_encontrado}")
        print(f"   - Nuevo Estado: **disponible**")
        print(f"   - Fecha de devolución registrada: {fecha_devolucion_hoy}")
        print(f"   - El equipo ha sido desvinculado del estudiante.")
    except IOError as e:
        print(f"❌ Error al guardar los cambios en el archivo JSON: {e}")
=======
    guardar_json(archivo, prestamos)
    print(f"\n✅ ¡Devolución completada con éxito y guardada en '{archivo}'!")
>>>>>>> 2c3b56e92cc69e7b0f462fb69046e189b81e821f
