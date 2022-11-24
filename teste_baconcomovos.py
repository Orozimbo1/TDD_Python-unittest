"""
TDD - Test driven developments (Desenolvimento dirigido a testes)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o teste e ver passar

Refactor
Parte 3 -> Refatorar o codigo
"""
import unittest
from baconcomovos import bacon_com_ovos

class TesteBaconComOvos(unittest.TestCase):
    def teste_bacon_com_ovos_deve_retornar_assertion_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
           bacon_com_ovos('')

    def teste_bacon_com_ovos_deve_retornar_bacom_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def teste_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (4, 1, 7, 11)
        saida = 'Passa fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def teste_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def teste_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_3(self):
        entradas = (5, 10, 20, 25)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

unittest.main(verbosity=2)