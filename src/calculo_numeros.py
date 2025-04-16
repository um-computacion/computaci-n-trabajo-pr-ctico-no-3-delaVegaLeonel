from exceptions import ingrese_numero
from exceptions import NumeroDebeSerPositivo
from exceptions import NumeroMenorA1Exception
from exceptions import NumeroMayorA10Exception

def main():
    """
    Programa principal que solicita números al usuario y muestra los resultados.
    """
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except ValueError as e:
            print(f"Error: {e}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break
        except NumeroMenorA1Exception as e:
            print(f"Error: {e}")
        except NumeroMayorA10Exception as e:
            print(f"Error: {e}")    
            

if __name__ == "__main__":
    main() 