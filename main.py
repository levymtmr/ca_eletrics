from ca_analises import Ca

ca = Ca(v_peak=240, v_angle=65, i_peak=6, i_angle=30, frequency=40)

ca.circulo_angular()
ca.fator_de_potencia()
ca.plot_tensao_corrente()
ca.triangulo_potencias()

ca.draw()