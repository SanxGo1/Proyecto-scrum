def registrar_estudiante_interactivo(archivo="estudiantes.json"):
    """
    Pregunta al usuario los datos por consola, valida duplicados de documento
    y correo, y los guarda de forma persistente en un archivo JSON.
    """
    print("\n--- Registro de Nuevos Estudiantes ---")
    
    # 1. Solicitar los datos al usuario por consola
    documento = input("Ingrese el número de documento: ").strip()
    nombre = input("Ingrese el nombre completo: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    programa = input("Ingrese el programa académico: ").strip()

    # Validar que no queden campos vacíos
    if not documento or not nombre or not correo or not programa:
        print("❌ Error: Todos los campos son obligatorios. Inténtalo de nuevo.")
        return

    # 2. Asegurar la existencia del archivo JSON o crearlo vacío si no existe
    if not os.path.exists(archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)

    # 3. Cargar los datos existentes de manera segura
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                estudiantes = {}
            else:
                estudiantes = json.loads(contenido)
    except (json.JSONDecodeError, IOError):
        estudiantes = {}

    # 4. Validar que no exista el mismo número de documento
    if documento in estudiantes:
        print(f"❌ Error: Ya existe un estudiante registrado con el documento {documento}.")
        return

    # 5. Validar que no exista el mismo correo electrónico en otro registro
    for doc_existente, datos in estudiantes.items():
        if datos.get("correo") == correo:
            print(f"❌ Error: El correo '{correo}' ya está registrado (Documento: {doc_existente}).")
            return

    # 6. Agregar el nuevo estudiante con todos sus campos
    estudiantes[documento] = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa_academico": programa
    }

    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(estudiantes, f, indent=4, ensure_ascii=False)
        print(f"✅ ¡Estudiante {nombre} registrado y guardado exitosamente en '{archivo}'!")
    except IOError as e:
        print(f"❌ Error al escribir en el archivo JSON: {e}")


if __name__ == "__main__":
    while True:
        registrar_estudiante_interactivo()
        
        continuar = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n¡Proceso finalizado. Saliendo del sistema...")
            break
