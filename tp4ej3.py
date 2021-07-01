########################################################
# Eimi Saiz - @EimiSaiz
# TP 4 - Eje. 3: Conversión de temperaturas
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def convertir_a_centigrados(fahrenheit):

    '''convierte temperatura en grados fahrenheit a grados celsius'''

    centigrados = (fahrenheit -32 ) * 5.0/9.0
    print(f'{fahrenheit:.2f} grados Fahrenheit son {centigrados:.2f} grados Celsius')

def convertir_a_fahrenheit(centigrados):

    '''convierte temperatura en grados celsius a fahrenheit'''

    fahrenheit = 9.0/5.0 * centigrados +32
    print(f'{centigrados:.2f} grados Celsius son {fahrenheit:.2f} grados Fahrenheit')

if __name__ == "__main__":
    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    centigrados = int(input('Ingrese la temperatura en grados Celsius: '))
    convertir_a_centigrados(fahrenheit)
    convertir_a_fahrenheit(centigrados)