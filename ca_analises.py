import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Ca:

    def __init__(self, v_peak, v_angle, i_peak, i_angle, frequency):
        self.v_peak = v_peak
        self.v_angle = v_angle
        self.i_peak = i_peak
        self.i_angle = i_angle
        self.frequency = frequency

    def _degrees_to_radians(self, degrees):
        return degrees * np.pi / 180

    def plot_tensao_corrente(self, v_peak, v_angle, i_peak, i_angle, frequency):
        # labels para as legendas dos graficos
        v_peak_label = v_peak
        v_angle_label = v_angle
        i_peak_label = i_peak
        i_angle_label = i_angle

        if frequency == 0.0:
            frequency = 1

        frequencia_angular = 2 * np.pi * frequency

        period = np.linspace(0, 1/frequency, 1000)

        tensao_instantanea = v_peak * np.sin(frequencia_angular * period + np.deg2rad(v_angle))
        current = i_peak * np.sin(frequencia_angular * period + np.deg2rad(i_angle))

        plt.figure(figsize=(10, 6))

        # plot voltagem
        plt.plot(period, tensao_instantanea, label='AC Voltage')

        # plot current
        plt.plot(period, current, label='Current ({}A Peak, {}° Phase Angle)'.format(i_peak_label, i_angle_label), color='green')

        plt.axhline(y=0, color='k', linestyle='--')  # zero line
        plt.axvline(x=v_angle/360/frequency, color='r', linestyle='--', label='Phase Voltage Angle at {}°'.format(v_angle_label))
        plt.axvline(x=i_angle/360/frequency, color='purple', linestyle='--', label='Current Phase Angle at {}°'.format(i_angle_label))

        # Setting precise voltage axis divisions
        plt.yticks(np.arange(-v_peak, v_peak + 1, 20))

        # detalhes das legendas do grafico, como titulo e nome dos eixos
        plt.title('AC Voltage Signal with {}V Peak and {}° Phase Angle'.format(v_peak_label, v_angle_label))
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.legend()
        plt.grid(True)

        plt.show()

    def circulo_angular(self, v_angle, i_angle):
        angle_voltage = self._degrees_to_radians(v_angle)
        angle_current = self._degrees_to_radians(i_angle)

        # Setting up the plot
        plt.figure(figsize=(12, 7))
        ax = plt.subplot(111, polar=True)  # Create a polar subplot

        # Voltage angle
        ax.plot([0, angle_voltage], [0, 1], label='Voltage Phase Angle ({}°)'.format(v_angle), color='blue')

        # Current angle
        ax.plot([0, angle_current], [0, 1], label='Current Phase Angle ({}°)'.format(i_angle), color='green')

        # Additional plot settings
        ax.set_theta_zero_location('E')  # Zero degrees at the right
        ax.set_theta_direction(-1)  # Clockwise direction
        ax.set_ylim(0, 1)  # Limit the radius

        # Adding a legend and title
        plt.title('Comparison of Phase Angles: Voltage vs Current')
        ax.legend(loc='upper right')

        plt.show()

    def fator_de_potencia(self, v_angle, i_angle):
        diferenca_entre_fases = v_angle - i_angle
        fp = np.cos(np.deg2rad(diferenca_entre_fases))
        data = {
            "Voltage Phase Angle (degrees)": [v_angle],
            "Current Phase Angle (degrees)": [i_angle],
            "Phase Difference (degrees)": [diferenca_entre_fases],
            "Power Factor": [fp]
        }

        df = pd.DataFrame(data)

        # Criar figura para a tabela
        fig, ax = plt.subplots(figsize=(6, 1))  # Tamanho da figura
        ax.axis('off')  # Ocultar os eixos

        # Adicionar tabela
        the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(10)  # Tamanho da fonte
        the_table.scale(1, 1.5)  # Ajustar escala da tabela

        # Mostrar a tabela
        plt.show()

    def triangulo_potencias(self, v_peak,v_angle, i_peak, i_angle):
        teta = v_angle - i_angle

        potencia_aparente = v_peak * i_peak
        potencia_reativa = potencia_aparente * np.sin(np.deg2rad(teta))
        potencia_ativa = potencia_aparente * np.cos(np.deg2rad(teta))

        plt.figure(figsize=(8, 6))
        plt.quiver(0, 0, potencia_ativa, 0, angles='xy', scale_units='xy', scale=1, color='r', label='Active Power (P)')
        plt.quiver(potencia_ativa, 0, 0, potencia_reativa, angles='xy', scale_units='xy', scale=1, color='b', label='Reactive Power (Q)')
        plt.quiver(0, 0, potencia_ativa, potencia_reativa, angles='xy', scale_units='xy', scale=1, color='g', label='Apparent Power (S)')

        # Setting the limits for better visualization
        plt.xlim(0, 1500)
        plt.ylim(0, 1500)

        # Adding labels and title
        plt.title('Power Triangle Angle {}°'.format(teta))
        plt.xlabel('Active Power (W)')
        plt.ylabel('Reactive Power (VAR)')
        plt.grid(True)
        plt.legend()

        plt.show()