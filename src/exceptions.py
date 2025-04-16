class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    pass

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        int: El número ingresado si es válido.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido") 
    
class NumeroMenorA1Exception(Exception):
    pass

class NumeroMayorA10Exception(Exception):
    pass

def calcular_1_al_10(numero = int):
    if(numero < 1):
        raise NumeroMenorA1Exception('numero es menor a 1')
    if(numero > 10):
        raise NumeroMayorA10Exception('numero es mayor a 10')
    print('tu numero ' + str(numero) + ' es del 1 al 10')

while True:
    try:
        numero = int(input('ingrese un numero del 1 al 10: '))
        calcular_1_al_10(numero)
        break
    except ValueError as value_error_excepcion:
        print("burro: por favor ingresa un numero")
    except NumeroMayorA10Exception as mi_excepcion:
        print("burro: " + str(mi_excepcion))
    except NumeroMenorA1Exception as mi_excepcion:
        print("burro: " + str(mi_excepcion))

