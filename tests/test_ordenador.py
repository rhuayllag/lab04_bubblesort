import unittest
from src.ordenador import Ordenador


class TestBubbleSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[SetUpClass] Inicio de la suite de bubbleSort")

    @classmethod
    def tearDownClass(cls):
        print("\n[TearDownClass] Fin de la suite de bubbleSort")

    def setUp(self):
        # Inicializar el SUT (System Under Test)
        self.ordenador = Ordenador()

    def tearDown(self):
        # Liberar recursos
        del self.ordenador

    def test_cp1_un_elemento(self):
        # Arrange
        vet = [7]
        esperado = [7]
        # Act
        resultado = self.ordenador.bubble_sort(vet)
        # Assert
        self.assertEqual(esperado, resultado,
                         "CP1: una lista de un elemento no cambia")

    def test_cp2_ya_ordenado(self):
        vet = [1, 2]
        esperado = [1, 2]
        resultado = self.ordenador.bubble_sort(vet)
        self.assertEqual(esperado, resultado,
                         "CP2: una lista ordenada no cambia")

    def test_cp3_un_intercambio(self):
        vet = [2, 1]
        esperado = [1, 2]
        resultado = self.ordenador.bubble_sort(vet)
        self.assertEqual(esperado, resultado,
                         "CP3: debe intercambiar los dos elementos")

    def test_cp4_ciclo_externo_dos_veces(self):
        vet = [3, 1, 2]
        esperado = [1, 2, 3]
        resultado = self.ordenador.bubble_sort(vet)
        self.assertEqual(esperado, resultado,
                         "CP4: debe ordenar tres elementos")


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestBubbleSort))
    return s


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())