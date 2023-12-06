import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import cmath
import math


def request_complex_input(prompt):
    while True:
        try:
            real, imag = map(float, input(prompt).split(','))
            return complex(real, imag)
        except ValueError:
            print("Entrada inválida. Por favor, insira no formato 'real,imag'.")

def calculate_currents(van, vbn, vcn, zan, zbn, zcn):
    return van / zan, vbn / zbn, vcn / zcn

def calculate_power(v, i):
    return v * i.conjugate()

def calculate_power_factor_and_type(power):
    active_power = power.real
    apparent_power = abs(power)
    if apparent_power == 0:
        return 0, "Neutro"

    power_factor = active_power / apparent_power
    circuit_type = "Indutivo" if power_factor > 0 else "Capacitivo"
    return power_factor, circuit_type

def update_and_calculate():
    # Limpa a tabela antes de recalcular
    for i in tree.get_children():
        tree.delete(i)
    calculate_and_display()

def calculate_and_display():
    try:
        van = complex(*map(float, van_entry.get().split(',')))
        vbn = complex(*map(float, vbn_entry.get().split(',')))
        vcn = complex(*map(float, vcn_entry.get().split(',')))
        zan = complex(*map(float, zan_entry.get().split(',')))
        zbn = complex(*map(float, zbn_entry.get().split(',')))
        zcn = complex(*map(float, zcn_entry.get().split(',')))

        connection_type = connection_var.get()

        if connection_type == "Y-Y":
            ia, ib, ic = van / zan, vbn / zbn, vcn / zcn
        elif connection_type == "Y-Δ":
            # Para a ligação Y-Δ, ajustamos as tensões e correntes
            # A tensão de fase em Y é igual à tensão de linha em Δ
            # A corrente de linha em Δ é sqrt(3) vezes a corrente de fase em Y
            sqrt_3 = math.sqrt(3)
            ia, ib, ic = (van / zan) * sqrt_3, (vbn / zbn) * sqrt_3, (vcn / zcn) * sqrt_3

        # Função auxiliar para converter para coordenadas polares e formatar a saída
        def to_polar_str(complex_number):
            magnitude, angle = cmath.polar(complex_number)
            angle_deg = math.degrees(angle)  # Convertendo radianos para graus
            return f"{magnitude:.2f} ∠ {angle_deg:.2f}°"
        
        def to_absolute_str(complex_number):
            return f"{complex_number.real:.2f}"

        ia, ib, ic = van / zan, vbn / zbn, vcn / zcn
        pa, pb, pc = van * ia.real, vbn * ib.real, vcn * ic.real
        p_total = pa + pb + pc
        q_total = pa.imag + pb.imag + pc.imag

        pf_a, type_a = calculate_power_factor_and_type(pa)
        pf_b, type_b = calculate_power_factor_and_type(pb)
        pf_c, type_c = calculate_power_factor_and_type(pc)
        pf_total, type_total = calculate_power_factor_and_type(p_total)

        for i in tree.get_children():
            tree.delete(i)

        # Adicionando os resultados na tabela, convertidos para coordenadas polares
        tree.insert("", "end", values=("Ia", to_polar_str(ia)))
        tree.insert("", "end", values=("Ib", to_polar_str(ib)))
        tree.insert("", "end", values=("Ic", to_polar_str(ic)))
        tree.insert("", "end", values=("Pa", to_absolute_str(pa)))
        tree.insert("", "end", values=("Pb", to_absolute_str(pb)))
        tree.insert("", "end", values=("Pc", to_absolute_str(pc)))
        tree.insert("", "end", values=("Ptotal", to_polar_str(p_total)))
        tree.insert("", "end", values=("Qtotal", q_total))  # Qtotal permanece como está, já que é um valor real
        tree.insert("", "end", values=("PFa", f"{pf_a} ({type_a})"))
        tree.insert("", "end", values=("PFb", f"{pf_b} ({type_b})"))
        tree.insert("", "end", values=("PFc", f"{pf_c} ({type_c})"))
        tree.insert("", "end", values=("PFtotal", f"{pf_total} ({type_total})"))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira os valores corretos.")


# Configuração da janela Tkinter
root = tk.Tk()
root.title("Cálculo de Circuitos Trifásicos")

connection_var = tk.StringVar(value="Y-Y")  # Valor padrão

ttk.Radiobutton(root, text="Estrela-Estrela (Y-Y)", variable=connection_var, value="Y-Y").pack()
ttk.Radiobutton(root, text="Estrela-Delta (Y-Δ)", variable=connection_var, value="Y-Δ").pack()

van_entry = tk.Entry(root)
vbn_entry = tk.Entry(root)
vcn_entry = tk.Entry(root)
zan_entry = tk.Entry(root)
zbn_entry = tk.Entry(root)
zcn_entry = tk.Entry(root)

tk.Label(root, text="Van (real,imag):").pack()
van_entry.pack()
tk.Label(root, text="Vbn (real,imag):").pack()
vbn_entry.pack()
tk.Label(root, text="Vcn (real,imag):").pack()
vcn_entry.pack()
tk.Label(root, text="Zan (real,imag):").pack()
zan_entry.pack()
tk.Label(root, text="Zbn (real,imag):").pack()
zbn_entry.pack()
tk.Label(root, text="Zcn (real,imag):").pack()
zcn_entry.pack()

calculate_button = tk.Button(root, text="Calcular", command=update_and_calculate)
calculate_button.pack()

# Configuração da tabela (Treeview)
columns = ("Parâmetro", "Valor")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Parâmetro", text="Parâmetro")
tree.heading("Valor", text="Valor")
tree.pack()


root.mainloop()