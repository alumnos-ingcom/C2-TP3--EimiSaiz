########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 1: Ingreso de números enteros
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def ingreso_entero_reintento():
    intentos = 0
    while intentos < 5:
        valor = input("Ingrese un número entero.\n")
        try:
            valor = int(valor)
            return valor
        except ValueError as err:
            intentos = intentos + 1
            raise IngresoIncorrecto("Lo siento, no entendí.\n") from err
    if intentos == 5:
        print("Se superó la cantidad máxima de intentos.\n")
    else:
        pass

def ingreso_entero_restringido(numero, valorA, valorB):
    numero_mayor = 0
    numero_menor = 0
    if valorA < valorB:
        numero_mayor = valorB
        numero_menor = valorA
    else:
        numero_mayor = valorA
        numero_menor = valorB
    if numero >= numero_menor and numero <= numero_mayor:
        return True
    else:
        return False

def prueba():
    valorA = int(input("Ingrese un número.\n"))
    valorB = int(input("Ingrese otro número.\n"))
    numero = int(input("Ingrese un número entre los números anteriormente ingresados.\n"))
    resultado_restrigido = ingreso_entero_restringido(numero, valorA, valorB)
    resultado_reintento = ingreso_entero_reintento()
    
    ingreso_entero_restringido(numero, valorA, valorB)
    ingreso_entero_reintento()
    
    print(resultado_restrigido)
    print(resultado_reintento)
    
if __name__ == "__main__":
    prueba()
