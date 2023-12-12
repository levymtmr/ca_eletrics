import math
import cmath
import numpy as np

def complex_to_polar(complex_number: complex):
    magnitude, angulo_rad = cmath.polar(complex_number)
    angle_degree = math.degrees(angulo_rad)
    return (magnitude, angle_degree)

def converter_polar_para_retangular(polar):
    modulo, angulo = polar
    # A função rect recebe argumentos em termos de (módulo, ângulo em radianos)
    # Portanto, é necessário converter o ângulo de graus para radianos
    angulo_radianos = math.radians(angulo)
    return cmath.rect(modulo, angulo_radianos)

def polar_division(a, b):
    real = a[0] / b[0]
    angle = a[1] - b[1]
    return (real, angle)

def start_current(tension: complex, impendancy: complex) -> (float, float):
    polar_tension = complex_to_polar(tension)
    polar_impendancy = complex_to_polar(impendancy)
    polar_current = polar_division(polar_tension, polar_impendancy)
    return polar_current

def delta_current(tension: complex, impendancy: complex):
    polar_inpendancy = complex_to_polar(impendancy)
    current = polar_division(tension, polar_inpendancy)
    return current

def phase_tension_to_line_tension(tension: complex):
    convert_tension = complex_to_polar(tension)
    module = convert_tension[0]
    angle = convert_tension[1]
    line_tension = module * math.sqrt(3)
    line_angle = angle + 30
    return (line_tension, line_angle)

def formatar_valor(valor):
    if isinstance(valor, complex):
        return complex(round(valor.real, 5), round(valor.imag, 5))
    elif isinstance(valor, tuple):
        # Arredondar cada elemento da tupla separadamente
        return tuple(round(v, 5) for v in valor)
    else:
        return round(valor, 5)
    
def calculate_power(polar_tension, polar_current):
    tension = polar_tension[0]
    tension_angle = polar_tension[1]
    current = polar_current[0]
    current_angle = polar_current[1]
    
    angle = math.radians(tension_angle - current_angle)
    angle_cos = math.cos(angle)

    power = tension * current * angle_cos

    return power

def calculate_delta_power(polar_tension, line_current):
    tension = polar_tension[0]
    current = line_current[0]
    angle = polar_tension[1] - line_current[1]
    return (tension * current * math.cos(angle))


def calculate_reative_power(polar_tension, polar_current):
    tension = polar_tension[0]
    tension_angle = polar_tension[1]
    current = polar_current[0]
    current_angle = polar_current[1]
    
    angle = math.radians(tension_angle - current_angle)
    angle_cos = math.sin(angle)

    power = tension * current * angle_cos

    return power

def calculate_reative_delta_power(polar_tension, line_current):
    tension = polar_tension[0]
    current = line_current[0]
    angle = polar_tension[1] - line_current[1]
    return (tension * current * math.sin(angle))

def calculate_estrela_estrela(entries):
    resultados = {}
    try:
        # Converter entradas para complexos
        Van_polar = tuple(map(float, entries['Van'].get().split(',')))
        Vbn_polar = tuple(map(float, entries['Vbn'].get().split(',')))
        Vcn_polar = tuple(map(float, entries['Vcn'].get().split(',')))

        # Converter coordenadas polares para retangulares
        Van = converter_polar_para_retangular(Van_polar)
        Vbn = converter_polar_para_retangular(Vbn_polar)
        Vcn = converter_polar_para_retangular(Vcn_polar)

        Zan = complex(*map(float, entries['Zan'].get().split(',')))
        Zbn = complex(*map(float, entries['Zbn'].get().split(',')))
        Zcn = complex(*map(float, entries['Zcn'].get().split(',')))

        # correntes       
        Ia = start_current(Van, Zan)
        Ib = start_current(Vbn, Zbn)
        Ic = start_current(Vcn, Zcn)
        
        # Calcular potências médias nos ramos
        Pa = calculate_power(complex_to_polar(Van), Ia)
        Pb = calculate_power(complex_to_polar(Vbn), Ib)
        Pc = calculate_power(complex_to_polar(Vcn), Ic)

        # Potência total
        Pt = Pa + Pb + Pc

        # Potências reativas
        Qa = calculate_reative_power(complex_to_polar(Van), Ia)
        Qb = calculate_reative_power(complex_to_polar(Vbn), Ib)
        Qc = calculate_reative_power(complex_to_polar(Vcn), Ic)

        Qt = Qa + Qb + Qc

        potencia_aparente = math.sqrt((Pt**2) + (Qt**2))

        # Fator de potência
        FP = Pt / (Pt ** 2 + (Qa + Qb + Qc) ** 2) ** 0.5
        natureza = "Indutiva" if FP > 0 else "Capacitiva"

        # Armazenar os resultados
        resultados = {
            'Ia': "{} (A)".format(formatar_valor(Ia)),
            'Ib': "{} (A)".format(formatar_valor(Ib)),
            'Ic': "{} (A)".format(formatar_valor(Ic)),
            'Pa': "{} (W)".format(formatar_valor(Pa)),
            'Pb': "{} (W)".format(formatar_valor(Pb)),
            'Pc': "{} (W)".format(formatar_valor(Pc)),
            'Pt': "{} (W)".format(formatar_valor(Pt)),
            'Qa': "{} (VAr)".format(formatar_valor(Qa)),
            'Qb': "{} (VAr)".format(formatar_valor(Qb)),
            'Qc': "{} (VAr)".format(formatar_valor(Qc)),
            'Qt': "{} (VAr)".format(formatar_valor(Qt)),
            'St': "{} (VA)".format(formatar_valor(potencia_aparente)),
            # A natureza do FP (indutiva/capacitiva) permanece como uma string
            'FP': formatar_valor(FP),
            "natureza": natureza
        }
    except ValueError:
        print("Verifique as entradas. Elas devem ser números separados por vírgulas.")

    return resultados

def calculate_delta_estrela(entries):
    resultados = {}
    try:
        # Converter entradas para complexos
        Van_polar = tuple(map(float, entries['Van'].get().split(',')))
        Vbn_polar = tuple(map(float, entries['Vbn'].get().split(',')))
        Vcn_polar = tuple(map(float, entries['Vcn'].get().split(',')))

        # Converter coordenadas polares para retangulares
        Van = converter_polar_para_retangular(Van_polar)
        Vbn = converter_polar_para_retangular(Vbn_polar)
        Vcn = converter_polar_para_retangular(Vcn_polar)

        # Transformando para tensao de linha
        Vab = phase_tension_to_line_tension(Van)
        Vbc = phase_tension_to_line_tension(Vbn)
        Vca = phase_tension_to_line_tension(Vcn)

        Zan = complex(*map(float, entries['Zan'].get().split(',')))
        Zbn = complex(*map(float, entries['Zbn'].get().split(',')))
        Zcn = complex(*map(float, entries['Zcn'].get().split(',')))

        # correntes       
        Ia = delta_current(Vab, Zbn)
        Ib = delta_current(Vbc, Zan)
        Ic = delta_current(Vca, Zcn)

        # Calcular potências médias nos ramos
        Pa = calculate_delta_power(Vab, Ia)
        Pb = calculate_power(Vbc, Ib)
        Pc = calculate_power(Vca, Ic)

        # Potência total
        Pt = Pa + Pb + Pc

        # Potências reativas
        Qa = calculate_reative_power(Vab, Ia)
        Qb = calculate_reative_power(Vbc, Ib)
        Qc = calculate_reative_power(Vca, Ic)

        Qt = Qa + Qb + Qc

        potencia_aparente = math.sqrt((Pt**2) + (Qt**2))

        # Fator de potência
        FP = Pt / (Pt ** 2 + (Qa + Qb + Qc) ** 2) ** 0.5
        natureza = "Indutiva" if FP > 0 else "Capacitiva"

        # Armazenar os resultados
        resultados = {
            'Ia': formatar_valor(Ia),
            'Ib': formatar_valor(Ib),
            'Ic': formatar_valor(Ic),
            'Pa': formatar_valor(Pa),
            'Pb': formatar_valor(Pb),
            'Pc': formatar_valor(Pc),
            'Pt': formatar_valor(Pt),
            'Qa': formatar_valor(Qa),
            'Qb': formatar_valor(Qb),
            'Qc': formatar_valor(Qc),
            'Qt': formatar_valor(Qt),
            'St': formatar_valor(potencia_aparente),
            # A natureza do FP (indutiva/capacitiva) permanece como uma string
            'FP': formatar_valor(FP),
            "natureza": natureza
        }

    except ValueError:
        print("Verifique as entradas. Elas devem ser números separados por vírgulas.")

    return resultados
