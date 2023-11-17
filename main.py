from ca_analises import Ca
from interface import Interface

ca = Ca(v_peak=240, v_angle=65, i_peak=6, i_angle=30, frequency=40)

gui = Interface(ca.plot_tensao_corrente, ca.circulo_angular, ca.fator_de_potencia, ca.triangulo_potencias)

gui.start()
