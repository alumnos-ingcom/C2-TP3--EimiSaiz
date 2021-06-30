########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 7: Restas sucesivas
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

from tp4ej5 import ingreso_numero

def division_lenta(dividendo, divisor):
    if (divisor == 0) : print("Error, division por cero \n")
    elif (dividendo < divisor):
        cociente = 0; residuo = 0;
        print(f'El cociente es:{cociente} y el resto es:{residuo}')
    else:
        cociente = 0; residuo = 0
        while(residuo >= 0):
            if(dividendo - divisor < 0): break
            else:
                residuo = dividendo - divisor
                cociente = cociente + 1
                dividendo = residuo
        print(f'El cociente es:{cociente} y el resto es:{residuo}')


def prueba():
    dividendo = ingreso_numero("Ingresar dividendo:")
    divisor = ingreso_numero("Ingresar divisor:")
    division_lenta(dividendo, divisor)   

if __name__ == "__main__":
    prueba()         
