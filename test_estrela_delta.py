import unittest
from estrela_delta.operations import complex_to_polar, calculate_power, calculate_estrela_estrela, calculate_delta_estrela


# Mock classes para simular entradas e configurações
class MockEntry:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class MockConfig:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class TestarFuncoesCircuito(unittest.TestCase):

    def test_complex_to_polar(self):
        value1 = complex(10, 50)
        self.assertEqual("({:.4f},{:.4f})".format(complex_to_polar(value1)[
                         0], complex_to_polar(value1)[1]), "(50.9902,78.6901)")

        value2 = complex(-20, 30)
        self.assertEqual("({:.4f},{:.4f})".format(complex_to_polar(value2)[
                         0], complex_to_polar(value2)[1]), "(36.0555,123.6901)")

        value3 = complex(10, -12)
        self.assertEqual("({:.4f},{:.4f})".format(complex_to_polar(value3)[
                         0], complex_to_polar(value3)[1]), "(15.6205,-50.1944)")

        value4 = complex(34.5, -33.45)
        self.assertEqual("({:.4f},{:.4f})".format(complex_to_polar(value4)[
                         0], complex_to_polar(value4)[1]), "(48.0536,-44.1147)")

    def test_calculate_power(self):
        tension_1, current_1 = (220, 0), (17.179, -38.66)
        power1 = calculate_power(tension_1, current_1)
        self.assertEqual("{:.4f}".format(power1), '2951.1921')

        tension_2, current_2 = (220, 120), (15.8354, 89.744)
        power2 = calculate_power(tension_2, current_2)
        self.assertEqual("{:.4f}".format(power2), '3009.2360')

        tension_3, current_3 = (220, -120), (14.5380, -112.406)
        power3 = calculate_power(tension_3, current_3)
        self.assertEqual("{:.4f}".format(power3), '3170.3084')

    def test_calcular_valores_Y_Y(self):
        # Mock das entradas
        entries = {
            'Van': MockEntry('220,0'),
            'Vbn': MockEntry('-110,190.5255'),
            'Vcn': MockEntry('-110,-190.5255'),
            'Zan': MockEntry('10,8'),
            'Zbn': MockEntry('12,7'),
            'Zcn': MockEntry('15,-2')
        }

        # Resultados esperados
        expected_results = {'Ia': (17.17911, -38.65981), 'Ib': (15.83594, 89.74357), 'Ic': (14.538, -112.40537), 'Pa': 2951.21951, 'Pb': 3009.32432, 'Pc': 3170.30346,
                            'Pt': 9130.84729, 'Qa': 2360.97561, 'Qb': 1755.43919, 'Qc': -422.70713, 'Qt': 3693.70767, 'PotApar': 9849.66236, 'FP': 0.92702, 'natureza': 'Indutiva'}

        # Chamar a função calcular_valores
        results = calculate_estrela_estrela(entries)

        # Verificar se os resultados são como esperados
        for key in expected_results:
            self.assertAlmostEqual(results[key], expected_results[key])

        # Mock das entradas
        entries = {
            'Van': MockEntry('100,0'),
            'Vbn': MockEntry('-50,86.6025'),
            'Vcn': MockEntry('-50,-86.6025'),
            'Zan': MockEntry('15,0'),
            'Zbn': MockEntry('10,5'),
            'Zcn': MockEntry('6,-8')
        }

        # Resultados esperados
        expected_results = {
            # Coloque aqui os resultados esperados para este cenário de teste
        }

        # Chamar a função calcular_valores
        results = calculate_estrela_estrela(entries)

        # Verificar se os resultados são como esperados
        for key in expected_results:
            self.assertAlmostEqual(results[key], expected_results[key])

    def test_calcular_valores_delta_Y(self):
        # Mock das entradas
        entries = {
            'Van': MockEntry('220, 0'),
            'Vbn': MockEntry('-110,190.5255'),
            'Vcn': MockEntry('-110,-190.5255'),
            'Zan': MockEntry('8,4'),
            'Zbn': MockEntry('8,4'),
            'Zcn': MockEntry('8,4')
        }

        # Resultados esperados
        expected_results = {
            # Coloque aqui os resultados esperados para este cenário de teste
        }

        # Chamar a função calcular_valores
        results = calculate_delta_estrela(entries)

        # Verificar se os resultados são como esperados
        for key in expected_results:
            self.assertAlmostEqual(results[key], expected_results[key])


if __name__ == '__main__':
    unittest.main()
