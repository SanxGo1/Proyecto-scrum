from datetime import datetime

def procesar_devolucion_computador(archivo="prestamos.json"):
    print("\n--- Módulo de Devolución de Computadores ---")
    
    if not os.path.exists(archivo):
        print(f"❌ Error: El archivo '{archivo}' no existe.")
        return

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            prestamos = json.loads(contenido) if contenido else {}
    except (json.JSONDecodeError, IOError):
        print(f"❌ Error al leer o procesar el archivo '{archivo}'.")
        return

    cedula_buscar = input("Ingrese el número de cédula del estudiante: ").strip()
    
    if not cedula_buscar:
        print("❌ Error: Debe ingresar un número de cédula válido.")
        return

    equipos_del_usuario = []
    for codigo_pc, info in prestamos.items():
        if info.get("estado") == "ocupado" and str(info.get("documento")) == cedula_buscar:
            equipos_del_usuario.append((codigo_pc, info))

    if not equipos_del_usuario:
        print(f"❌ La cédula '{cedula_buscar}' no registra ningún computador en estado 'ocupado'.")
        return

    print(f"\n🔍 ¡Equipos encontrados para el documento {cedula_buscar}:")
    for codigo_pc, info in equipos_del_usuario:
        print(f"   💻 Equipo: {codigo_pc} | Estudiante: {info.get('nombre')} | Fecha de Préstamo: {info.get('fecha_prestamo')}")

    codigo_ingresado = input("\nIngrese el código numérico del computador que va a devolver: ").strip()
    
    codigo_encontrado = None
    for codigo_pc, info in equipos_del_usuario:
        if codigo_ingresado in codigo_pc:
            codigo_encontrado = codigo_pc
            break

    if not codigo_encontrado:
        print("❌ El código ingresado no coincide con los equipos pendientes de este estudiante.")
        return

    confirmar = input(f"¿Confirma que desea procesar la devolución del equipo {codigo_encontrado}? (s/n): ").strip().lower()
    if confirmar != 's':
        print("⚠️ Operación de devolución cancelada.")
        return

    fecha_devolucion_hoy = datetime.now().strftime("%Y-%m-%d")

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
        print(f"\n✅ ¡Devolución completada con éxito!")
        print(f"   - Equipo: {codigo_encontrado}")
        print(f"   - Nuevo Estado: **disponible**")
        print(f"   - Fecha de devolución registrada: {fecha_devolucion_hoy}")
        print(f"   - El equipo ha sido desvinculado del estudiante.")
    except IOError as e:
        print(f"❌ Error al guardar los cambios en el archivo JSON: {e}")