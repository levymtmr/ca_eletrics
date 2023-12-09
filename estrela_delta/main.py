import tkinter as tk
from tkinter import ttk
from operations import calculate_estrela_estrela, calculate_delta_estrela


def calcular_valores(entries, config):
    try:
        # Converter entradas para complexos
        Van = complex(*map(float, entries['Van'].get().split(',')))
        Vbn = complex(*map(float, entries['Vbn'].get().split(',')))
        Vcn = complex(*map(float, entries['Vcn'].get().split(',')))
        Zan = complex(*map(float, entries['Zan'].get().split(',')))
        Zbn = complex(*map(float, entries['Zbn'].get().split(',')))
        Zcn = complex(*map(float, entries['Zcn'].get().split(',')))

        # Cálculo diferenciado com base na configuração
        if config.get() == "Y-Y":
            return calculate_estrela_estrela(entries=entries)
        elif config.get() == "Y-D":
            return calculate_delta_estrela(entries=entries)
        else:
            raise ValueError("Configuração de circuito não selecionada")

    except ValueError:
        print("Verifique as entradas. Elas devem ser números separados por vírgulas.")

def limpar_campos(entries, results):
    for entry in entries.values():
        entry.delete(0, tk.END)
    for result in results.values():
        result.set("")

def atualizar_resultados(resultados, results):
    for chave, valor in resultados.items():
        results[chave].set(str(valor))


# Configuração da janela principal
root = tk.Tk()
root.title("Cálculos de Circuitos Trifásicos")

# Criar campos de entrada
entries = {}
for label in ["Van", "Vbn", "Vcn", "Zan", "Zbn", "Zcn"]:
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=5, fill='x')
    ttk.Label(frame, text=label).pack(side='left')
    entry = ttk.Entry(frame)
    entry.pack(side='right', expand=True, fill='x')
    entries[label] = entry

# Adicionar botões de opção para a configuração do circuito
config_var = tk.StringVar(value="Y-Y")  # Valor padrão
ttk.Radiobutton(root, text="Estrela-Estrela",
                variable=config_var, value="Y-Y").pack()
ttk.Radiobutton(root, text="Delta-Estrela",
                variable=config_var, value="Y-D").pack()

# Botões para calcular e limpar
results = {label: tk.StringVar() for label in [
    "Ia", "Ib", "Ic", "Pa", "Pb", "Pc", "Pt", "Qa", "Qb", "Qc", "Qt", "PotApar","FP", "natureza"]}
ttk.Button(root, text="Calcular", command=lambda: atualizar_resultados(
    calcular_valores(entries, config_var), results)).pack(pady=5)
ttk.Button(root, text="Limpar", command=lambda: limpar_campos(
    entries, results)).pack(pady=5)

# Campos para mostrar os resultados
for label in results:
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=5, fill='x')
    ttk.Label(frame, text=label).pack(side='left')
    ttk.Label(frame, textvariable=results[label]).pack(side='right')

# Executar a janela principal
root.mainloop()
