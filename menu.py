

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from registroequipos import registrar_equipo
from consultarequipos import consultar_equipos
import consola as consola






def menu():
	consola.limpiar_pantalla()
	while True:
		print("\n--- MENÚ ---")
		print("1. Registrar equipo")
		print("2. Consultar equipos")
		print("3. Salir")

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
			print("Hasta luego.")
			consola.pausa()
			break
		else:
			print("Opción no válida.")
			consola.pausa()
			consola.limpiar_pantalla()


if __name__ == "__main__":
	menu()