import unittest
from src.exceptions import (
    ingrese_numero, calcular_1_al_10,
    NumeroDebeSerPositivo, 
    NumeroMenorA1Exception, 
    NumeroMayorA10Exception
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='AAA'
    )
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

class TestNumerosDel1al10(unittest.TestCase):
    
    def test_feliz(self):
        result = calcular_1_al_10(5)
        self.assertEqual(
            result,
            "tu numero "+ str(5) + "es del 1 al 10"
        )
    def test_da_error_numero_es_menor_1(self):
        with self.assertRaises(NumeroMenorA1Exception):
            result = calcular_1_al_10(-14)

    def test_da_error_numero_es_mayor_10(self):
        with self.assertRaises(NumeroMayorA10Exception):
            result = calcular_1_al_10(14)


if __name__ == '__main__':
    unittest.main() 