"""
class Pessoa:
    __init__:
        nome str
        sobrenome str
        dados_obtidos bool
    
    API:
        obter_todos_os_dados -> method
            OK
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from unittest.mock import patch
from Pessoa import Pessoa

class testePessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Matheus', 'Orozimbo')

    def teste_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Matheus')

    def teste_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def teste_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Orozimbo')

    def teste_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def teste_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def teste_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

        self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
        self.assertTrue(self.p1.dados_obtidos)

if __name__ == "__main__":
    unittest.main(verbosity=2)
