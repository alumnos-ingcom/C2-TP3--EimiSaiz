########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 9: Números primos
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

from tp4ej5 import ingreso_numero

def es_primo(numero):
    numero = abs(numero)
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

if __name__ == "__main__":
    numero = ingreso_numero("Ingresar un numero:")
    es_primo(numero)