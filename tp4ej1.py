########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 1: Ingreso de números enteros
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def ingreso_entero(mensaje):
    ingreso = input(mensaje + "Ingrese un número.\n")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No es un número.") from err
    return entero


def prueba():
    ingreso_entero("Ingresar un numero entero.\n")
    pass

if __name__ == "__main__":
    prueba()