########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 5: Números positivos y negativos
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def ingreso_numero(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except Exception as ex:
        print("Ha habido una excepción", type(ex))
    else:
        print("No ha ocurrido ninguna excepción")
        return entero


def signo(numero):
    if numero == 0: print(f'Numero:{numero} Neutro')
    elif numero < 0: print(f'Numero:{numero} Negativo')
    else: return print(f'Numero:{numero} Positivo')
 
if __name__ == "__main__":
    numero = ingreso_numero("Ingresar un numero entero:")
    signo(numero)