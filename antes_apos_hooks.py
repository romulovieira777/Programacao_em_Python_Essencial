"""
Unitetest - Antes e após hooks


----
hooks - são os testes em si. Ou seja, a execução dos testes.
----


setup() -> é executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com
bancos de dados

"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setp
    pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar primeiro
        # tearDown() vai rodar depois.
        pass

    def testDown(self):
        # Configurações do tearDown
        pass
