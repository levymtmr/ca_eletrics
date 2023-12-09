import math
import cmath
import numpy as np

def complex_to_polar(complex_number: complex):
    magnitude, angulo_rad = cmath.polar(complex_number)
    angle_degree = math.degrees(angulo_rad)
    return (magnitude, angle_degree)

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
    polar_tension = complex_to_polar(tension)
    phase_tension = (math.sqrt(3) * polar_tension[0], polar_tension[1] + 30)
    polar_impendancy = complex_to_polar(impendancy)
    current_polar = polar_division(phase_tension, polar_impendancy)
    return current_polar

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

def calculate_reative_power(polar_tension, polar_current):
    tension = polar_tension[0]
    tension_angle = polar_tension[1]
    current = polar_current[0]
    current_angle = polar_current[1]
    
    angle = math.radians(tension_angle - current_angle)
    angle_cos = math.sin(angle)

    power = tension * current * angle_cos

    return power

def calculate_estrela_estrela(entries):
    resultados = {}
    try:
        # Converter entradas para complexos
        Van = complex(*map(float, entries['Van'].get().split(',')))
        Vbn = complex(*map(float, entries['Vbn'].get().split(',')))
        Vcn = complex(*map(float, entries['Vcn'].get().split(',')))
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
            'PotApar': formatar_valor(potencia_aparente),
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
        Van = complex(*map(float, entries['Van'].get().split(',')))
        Vbn = complex(*map(float, entries['Vbn'].get().split(',')))
        Vcn = complex(*map(float, entries['Vcn'].get().split(',')))
        Zan = complex(*map(float, entries['Zan'].get().split(',')))
        Zbn = complex(*map(float, entries['Zbn'].get().split(',')))
        Zcn = complex(*map(float, entries['Zcn'].get().split(',')))

        # correntes       
        Ia = delta_current(Van, Zan)
        Ib = delta_current(Vbn, Zbn)
        Ic = delta_current(Vcn, Zcn)
        

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
            'PotApar': formatar_valor(potencia_aparente),
            # A natureza do FP (indutiva/capacitiva) permanece como uma string
            'FP': formatar_valor(FP),
            "natureza": natureza
        }

    except ValueError:
        print("Verifique as entradas. Elas devem ser números separados por vírgulas.")

    return resultados