import re
from guardar_datos import cargar_json, guardar_json

ARCHIVO_ESTUDIANTES = "estudiantes.json"

def registrar_estudiante_interactivo(archivo=ARCHIVO_ESTUDIANTES):
    print("\n--- Registro de Nuevos Estudiantes ---")

    estudiantes = cargar_json(archivo, {})

    while True:
        documento = input("Ingrese el número de documento (6 a 10 dígitos): ").strip()
        if not documento.isdigit():
            print("❌ Error: El documento debe contener únicamente números.")
        elif not (6 <= len(documento) <= 10):
            print("❌ Error: El documento debe tener entre 6 y 10 caracteres.")
        elif documento in estudiantes:
            print(f"❌ Error: Ya existe un estudiante registrado con el documento {documento}.")
        else:
            break

    while True:
        nombre = input("Ingrese el nombre completo: ").strip().upper()
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío.")
        elif not re.match(r"^[A-ZÁÉÍÓÚÑ\s]+$", nombre):
            print("❌ Error: El nombre solo debe contener letras.")
        else:
            break

    while True:
        correo = input("Ingrese el correo electrónico: ").strip()
        correo_duplicado = False
        for doc_existente, datos in estudiantes.items():
            if isinstance(datos, dict) and datos.get("correo") == correo:
                print(f"❌ Error: El correo '{correo}' ya está registrado (Documento: {doc_existente}).")
                correo_duplicado = True
                break
        
        if correo_duplicado:
            continue

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", correo):
            print("❌ Error: Ingrese un correo electrónico válido.")
        else:
            break

    while True:
        programa = input("Ingrese el programa académico: ").strip()
        if not programa:
            print("❌ Error: El programa académico no puede estar vacío.")
        elif not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", programa):
            print("❌ Error: El programa académico solo debe contener letras.")
        else:
            break

    estudiantes[documento] = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa_academico": programa
    }

    guardar_json(archivo, estudiantes)
    print(f"\n✅ Estudiante {nombre} registrado con éxito en '{archivo}'.")
    return True

def menu_registro_estudiantes():
    while True:
        registrar_estudiante_interactivo()

        continuar = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n¡Proceso de registro finalizado!")
            break

if __name__ == "__main__":
    menu_registro_estudiantes()