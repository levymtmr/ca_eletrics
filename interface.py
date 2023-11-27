import tkinter as tk

class Interface:
    def __init__(self, plot_tensao_corrente, circulo_angular, fator_de_potencia, triangulo_potencias, ligacao_estrela, ligacao_delta):
        self.plot_tensao_corrente = plot_tensao_corrente
        self.circulo_angular = circulo_angular
        self.fator_de_potencia = fator_de_potencia
        self.triangulo_potencias = triangulo_potencias
        self.ligacao_estrela = ligacao_estrela
        self.ligacao_delta = ligacao_delta
        self.root = tk.Tk()
        self.root.title("Gerador de graficos Ca")

        # Criando campos de entrada
        self.v_peak = tk.DoubleVar()
        self.v_angle = tk.DoubleVar()
        self.i_peak = tk.DoubleVar()
        self.i_angle = tk.DoubleVar()
        self.frequency = tk.DoubleVar()
        self.R = tk.DoubleVar()
        self.L = tk.DoubleVar()
        self.C = tk.DoubleVar()

        # Definindo labels e entradas para os parâmetros
        self.create_input_field("Tensão de pico (v_peak):", self.v_peak)
        self.create_input_field("Ângulo de Tensão (v_angle):", self.v_angle)
        self.create_input_field("Pico de Corrente (i_peak):", self.i_peak)
        self.create_input_field("Ângulo de Corrente (i_angle):", self.i_angle)
        self.create_input_field("Frequência (frequency):", self.frequency)
        self.create_input_field("Resistência (R):", self.R)
        self.create_input_field("Indutância (L):", self.L)
        self.create_input_field("Capacitância (C):", self.C)

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

        btn_ligacao_delta = tk.Button(self.root, text="Ligação Delta", command=lambda: self.call_ligacao_delta())
        btn_ligacao_delta.pack()

        btn_ligacao_estrela = tk.Button(self.root, text="Ligação Estrela", command=lambda: self.call_ligacao_estrela())
        btn_ligacao_estrela.pack()

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

    def call_ligacao_delta(self):
        params = self.get_input_values()
        R = params[5]
        L = params[6]
        C = params[7]

        if params:
            self.ligacao_delta(R, L, C)

    def call_ligacao_estrela(self):
        params = self.get_input_values()
        R = params[5]
        L = params[6]
        C = params[7]

        if params:
            self.ligacao_estrela(R, L, C)

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
        R = self.R.get()
        L = self.L.get()
        C = self.C.get()
        return v_peak, v_angle, i_peak, i_angle, frequency, R, L, C