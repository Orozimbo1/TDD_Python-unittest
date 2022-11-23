import unittest
from calculadora import soma, subtrai

class TesteCalculadora(unittest.TestCase):
    def teste_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def teste_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def teste_soma_varias_saidas(self):
        x_y_saidas = (
            (5, 5, 10),
            (15, 15, 30),
            (1.5, 5, 6.5),
            (-5, 15, 10),
            (25, 25, 50),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def teste_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('a', 10)

    def teste_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10, 'a')

    def teste_subtrai_5_e_15_deve_retornar_10(self):
        self.assertEqual(subtrai(5, 15), -10)

    def teste_subtrai_5_negativo_e_5_deve_retornar_10_negativo(self):
        self.assertEqual(subtrai(-5, 5), -10)

    def teste_subtrai_varias_saidas(self):
        x_y_saidas = (
            (5, 5, 0),
            (5, 15, -10),
            (1.5, 5, -3.5),
            (-5, 15, -20),
            (-25, 25, -50),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def teste_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('a', 10)

    def teste_subtrai_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(10, 'a')

if __name__ == '__main__':
    unittest.main(verbosity=2)