########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 2: Suma lenta
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

from tp4ej5 import ingreso_numero 

def suma_lenta(numero, otro_numero):
    suma = numero
    for i in range(abs(otro_numero)):
        if otro_numero < 0:
            aux = False
            suma = suma - 1
            unos_neg = (i+1)*"-1"
        else:
            aux = True
            suma = suma + 1
            unos_pos = (i+1)*"+1"
    if aux == False :        
        print(f'{numero}'+ unos_neg)
    else:
        print(f'{numero}'+ unos_pos)
    return suma


def prueba():
    numero = ingreso_numero("Ingresar numero:")
    otro_numero = ingreso_numero("Ingresar otro numero:")
    print(f'suma lenta : {suma_lenta(numero, otro_numero) }')

if __name__ == "__main__":
    prueba()
