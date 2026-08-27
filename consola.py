import sys
import subprocess


def limpiar_pantalla():
    if sys.platform.startswith("win"):
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)


def pausa(mensaje="Presione Enter para continuar..."):
    input(mensaje)


def despues_de_accion():
    pausa()
    limpiar_pantalla()
