import os
import sys


def limpiar_pantalla():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def pausa(mensaje="Presione Enter para continuar..."):
    input(mensaje)


def despues_de_accion():
    pausa()
    limpiar_pantalla()
