import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from registroequipos import registrar_equipo
from consultarequipos import consultar_equipos
import consola as consola
import registrar_estudiante
import prestamos
import devolucion 





def menu():
	consola.limpiar_pantalla()
	while True:
		print("\n--- MENÚ ---")
		print("1. Registrar equipo")
		print("2. Consultar equipos")
		print("3. Registrar estudiantes")
		print("4. Realizar préstamos")
		print("5. realizar devoluciones")
		print("6. Salir")


		opcion = input("Seleccione una opción: ")

		if opcion == "1":
			registrar_equipo()
			consola.pausa()
			consola.limpiar_pantalla()
		elif opcion == "2":
			consultar_equipos()
			consola.pausa()
			consola.limpiar_pantalla()
		elif opcion == "3":
			registrar_estudiante()
			consola.pausa()
			consola.limpiar_pantalla()
		elif opcion == "4":
			prestamos.registrar_prestamo()
			consola.pausa()
			consola.limpiar_pantalla()
		elif opcion == "5":
			devolucion.procesar_devolucion_computador()
			consola.pausa()
			consola.limpiar_pantalla()
		elif opcion == "6":
			print("Hasta luego.")
			consola.pausa()
			break
		else:
			print("Opción no válida.")
			consola.pausa()
			consola.limpiar_pantalla()


if __name__ == "__main__":
	menu()