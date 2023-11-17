import tkinter as tk

class Interface:
    def __init__(self, plot_tensao_corrente, circulo_angular, fator_de_potencia, triangulo_potencias):
        self.plot_tensao_corrente = plot_tensao_corrente
        self.circulo_angular = circulo_angular
        self.fator_de_potencia = fator_de_potencia
        self.triangulo_potencias = triangulo_potencias
        self.root = tk.Tk()
        self.root.title("Gerador de graficos Ca")

        # Criando campos de entrada
        self.v_peak = tk.DoubleVar()
        self.v_angle = tk.DoubleVar()
        self.i_peak = tk.DoubleVar()
        self.i_angle = tk.DoubleVar()
        self.frequency = tk.DoubleVar()

        # Definindo labels e entradas para os parâmetros
        self.create_input_field("Tensão de pico (v_peak):", self.v_peak)
        self.create_input_field("Ângulo de Tensão (v_angle):", self.v_angle)
        self.create_input_field("Pico de Corrente (i_peak):", self.i_peak)
        self.create_input_field("Ângulo de Corrente (i_angle):", self.i_angle)
        self.create_input_field("Frequência (frequency):", self.frequency)


    def start(self):
        btn_voltage_current = tk.Button(self.root, text="Gráfico de Tensão e Corrente",
                                        command=lambda: self.call_plot_voltage_current())
        btn_voltage_current.pack()

        btn_phase_graph = tk.Button(self.root, text="Gráfico de Fases", command=lambda: self.call_plot_circulo_angular())
        btn_phase_graph.pack()

        btn_power_triangle = tk.Button(self.root, text="Triângulo de Potência", command=lambda: self.call_plot_triangulo_de_potencias())
        btn_power_triangle.pack()

        btn_fator_de_potencia = tk.Button(self.root, text="Tabela Fator de potencia", command=lambda: self.call_plot_fator_de_potencia())
        btn_fator_de_potencia.pack()

        # Executar a GUI
        self.root.mainloop()

    def call_plot_voltage_current(self):
        # Desempacotar os valores da tupla e passar para a função plot_voltage_current
        params = self.get_input_values()
        v_peak = params[0]
        v_angle = params[1]
        i_peak = params[2]
        i_angle = params[3]
        frequency = params[4]

        if params:
            self.plot_tensao_corrente(v_peak, v_angle,i_peak, i_angle, frequency)
    
    def call_plot_circulo_angular(self):
        # Desempacotar os valores da tupla e passar para a função circulo_angular
        params = self.get_input_values()
        v_angle = params[1]
        i_angle = params[3]
        
        if params:
            self.circulo_angular(v_angle, i_angle)

    def call_plot_fator_de_potencia(self):
        params = self.get_input_values()
        v_angle = params[1]
        i_angle = params[3]
        
        if params:
            self.fator_de_potencia(v_angle, i_angle)

    def call_plot_triangulo_de_potencias(self):
        # Desempacotar os valores da tupla e passar para a função plot_voltage_current
        params = self.get_input_values()
        v_peak = params[0]
        v_angle = params[1]
        i_peak = params[2]
        i_angle = params[3]
        

        if params:
            self.triangulo_potencias(v_peak, v_angle,i_peak, i_angle)

    def create_input_field(self, label, variable):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=5)
        tk.Label(frame, text=label).pack(side=tk.LEFT)
        tk.Entry(frame, textvariable=variable).pack(side=tk.RIGHT)
        
    def get_input_values(self):
        v_peak = self.v_peak.get()
        v_angle = self.v_angle.get()
        i_peak = self.i_peak.get()
        i_angle = self.i_angle.get()
        frequency = self.frequency.get()
        return v_peak, v_angle, i_peak, i_angle, frequency