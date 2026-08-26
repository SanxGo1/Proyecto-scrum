<<<<<<< HEAD





import json
import os


def registrar_estudiante_interactivo(archivo="estudiantes.json"):
=======
from guardar_datos import cargar_json, guardar_json

ARCHIVO_ESTUDIANTES = "estudiantes.json"

def registrar_estudiante_interactivo():
>>>>>>> 2c3b56e92cc69e7b0f462fb69046e189b81e821f
    print("\n--- Registro de Nuevos Estudiantes ---")

    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                estudiantes = json.load(f)
        except (json.JSONDecodeError, OSError):
            estudiantes = {}
    else:
        estudiantes = {}
    
    estudiantes = cargar_json(ARCHIVO_ESTUDIANTES, {})

    documento = input("Ingrese el número de documento: ").strip()
    nombre = input("Ingrese el nombre completo: ").strip().upper()
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

<<<<<<< HEAD
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, ensure_ascii=False, indent=4)

    print(f"✅ Estudiante registrado correctamente en '{archivo}'.")



while True:
    registrar_estudiante_interactivo()

    continuar = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
    if continuar != 's':
        print("\n¡Proceso finalizado. Saliendo del sistema...")
        break
=======
    guardar_json(ARCHIVO_ESTUDIANTES, estudiantes)
    print(f"✅ Estudiante {nombre} registrado con éxito.")

if __name__ == "__main__":
    while True:
        registrar_estudiante_interactivo()
        continuar = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n¡Proceso finalizado. Saliendo del sistema...")
            break
>>>>>>> 2c3b56e92cc69e7b0f462fb69046e189b81e821f
