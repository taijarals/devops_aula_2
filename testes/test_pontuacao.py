import unittest

from pontuacao import calcular_pontuacao


class TestPontuacao(unittest.TestCase):
    def test_nenhuma_resposta_correta(self):
        self.assertEqual(calcular_pontuacao([1, 2, 3], [0, 1, 2]), 0)

    def test_uma_resposta_correta(self):
        self.assertEqual(calcular_pontuacao([0, 2, 3], [0, 1, 2]), 1)

    def test_tres_respostas_corretas(self):
        self.assertEqual(calcular_pontuacao([0, 1, 2], [0, 1, 2]), 3)

    def test_respostas_em_branco(self):
        self.assertEqual(calcular_pontuacao([None, None, None], [0, 1, 2]), 0)

    def test_respostas_ausentes(self):
        self.assertEqual(calcular_pontuacao([], [0, 1, 2]), 0)


if __name__ == "__main__":
    unittest.main()
