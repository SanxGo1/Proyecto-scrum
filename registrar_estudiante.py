import guardar_datos
def registrar_estudiante_interactivo(archivo="estudiantes.json"):
    print("\n--- Registro de Nuevos Estudiantes ---")
    
    documento = input("Ingrese el número de documento: ").strip()
    nombre = input("Ingrese el nombre completo: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    programa = input("Ingrese el programa académico: ").strip()

    if not documento or not nombre or not correo or not programa:
        print("❌ Error: Todos los campos son obligatorios. Inténtalo de nuevo.")
        return

    if documento in estudiantes:
        print(f"❌ Error: Ya existe un estudiante registrado con el documento {documento}.")
        return

    for doc_existente, datos in estudiantes.items():
        if datos.get("correo") == correo:
            print(f"❌ Error: El correo '{correo}' ya está registrado (Documento: {doc_existente}).")
            return

    estudiantes[documento] = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa_academico": programa
    }


if __name__ == "__main__":
    while True:
        registrar_estudiante_interactivo()
        
        continuar = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n¡Proceso finalizado. Saliendo del sistema...")
            break
